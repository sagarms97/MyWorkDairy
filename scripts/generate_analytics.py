import os
import re
from datetime import datetime
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def parse_worklogs():
    """
    Scans project directories for WorkLog.md and extracts structured task entries.
    """
    projects = {}
    
    for item in os.listdir(BASE_DIR):
        item_path = os.path.join(BASE_DIR, item)
        if os.path.isdir(item_path) and not item.startswith('.') and item not in ['scripts']:
            worklog_path = os.path.join(item_path, 'WorkLog.md')
            if os.path.isfile(worklog_path):
                with open(worklog_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                projects[item] = parse_markdown_content(content)
                
    return projects

def parse_markdown_content(content):
    """
    Extracts date sections and task details (Title, Status).
    """
    dates_data = defaultdict(lambda: {"completed": 0, "pending": 0, "tasks": []})
    
    date_blocks = re.split(r'##\s*📅\s*(\d{2}-\d{2}-\d{4})', content)
    
    if len(date_blocks) > 1:
        for i in range(1, len(date_blocks), 2):
            date_str = date_blocks[i].strip()
            block_text = date_blocks[i+1]
            
            task_blocks = re.split(r'###\s*🔹\s*Task\s*\d+:\s*', block_text)
            for t_block in task_blocks[1:]:
                lines = t_block.strip().split('\n')
                task_title = lines[0].strip()
                
                status = "Pending"
                if "Completed" in t_block:
                    status = "Completed"
                
                if status == "Completed":
                    dates_data[date_str]["completed"] += 1
                else:
                    dates_data[date_str]["pending"] += 1
                    
                dates_data[date_str]["tasks"].append({
                    "title": task_title,
                    "status": status
                })
                
    return dates_data

def generate_project_analytics(project_name, data):
    total_completed = sum(v["completed"] for v in data.values())
    total_pending = sum(v["pending"] for v in data.values())
    total_tasks = total_completed + total_pending
    rate = f"{(total_completed / total_tasks * 100):.1f}%" if total_tasks > 0 else "0.0%"
    
    # Sort dates chronologically
    sorted_dates = sorted(data.keys(), key=lambda d: datetime.strptime(d, "%d-%m-%Y"))
    
    lines = [
        f"# 📊 Task & Progress Analytics: {project_name}\n",
        f"> Auto-generated analytics report tracking tasks created, resolved, and pending.\n",
        "## 📈 Overall Metrics\n",
        f"- **Total Tasks**: `{total_tasks}`",
        f"- **Completed**: `{total_completed}` (✅)",
        f"- **Pending**: `{total_pending}` (⏳)",
        f"- **Resolution Rate**: `{rate}`\n",
        "```mermaid",
        "pie title Task Status Breakdown",
        f'    "Completed" : {total_completed if total_completed > 0 else 0.001}',
        f'    "Pending" : {total_pending if total_pending > 0 else 0.001}',
        "```\n",
        "## 📅 Daily Throughput\n",
        "| Date | Completed | Pending | Total | Status |",
        "| :---: | :---: | :---: | :---: | :---: |"
    ]
    
    # Reverse chronological for display
    for d in sorted(data.keys(), key=lambda x: datetime.strptime(x, "%d-%m-%Y"), reverse=True):
        c = data[d]["completed"]
        p = data[d]["pending"]
        t = c + p
        status_icon = "✅ All Done" if p == 0 else f"⏳ {p} In Progress"
        lines.append(f"| {d} | {c} | {p} | {t} | {status_icon} |")
        
    lines.append("\n```mermaid")
    lines.append("xychart-beta")
    lines.append(f'    title "Tasks Created vs Resolved by Date"')
    date_labels = [f'"{d}"' for d in sorted_dates]
    created_counts = [str(data[d]["completed"] + data[d]["pending"]) for d in sorted_dates]
    resolved_counts = [str(data[d]["completed"]) for d in sorted_dates]
    
    lines.append(f'    x-axis [{", ".join(date_labels)}]')
    lines.append('    y-axis "Number of Tasks" 0 --> 10')
    lines.append(f'    bar [{", ".join(created_counts)}]')
    lines.append(f'    line [{", ".join(resolved_counts)}]')
    lines.append("```\n")
    lines.append("*Bar: Total Created | Line: Resolved*\n")
    
    return "\n".join(lines)

def generate_global_summary(projects):
    global_total_c = 0
    global_total_p = 0
    
    daily_stats = defaultdict(lambda: {"completed": 0, "pending": 0})
    weekly_stats = defaultdict(lambda: {"completed": 0, "pending": 0})
    monthly_stats = defaultdict(lambda: {"completed": 0, "pending": 0})
    
    project_summary = []
    
    for proj_name, data in projects.items():
        p_c = sum(v["completed"] for v in data.values())
        p_p = sum(v["pending"] for v in data.values())
        p_tot = p_c + p_p
        p_rate = f"{(p_c / p_tot * 100):.1f}%" if p_tot > 0 else "0.0%"
        
        global_total_c += p_c
        global_total_p += p_p
        
        project_summary.append({
            "name": proj_name,
            "total": p_tot,
            "completed": p_c,
            "pending": p_p,
            "rate": p_rate
        })
        
        for d_str, counts in data.items():
            dt = datetime.strptime(d_str, "%d-%m-%Y")
            # Daily
            daily_stats[d_str]["completed"] += counts["completed"]
            daily_stats[d_str]["pending"] += counts["pending"]
            
            # Weekly (Year-Wxx)
            w_key = f"{dt.year}-W{dt.isocalendar()[1]:02d}"
            weekly_stats[w_key]["completed"] += counts["completed"]
            weekly_stats[w_key]["pending"] += counts["pending"]
            
            # Monthly (YYYY-MM)
            m_key = dt.strftime("%B %Y")
            monthly_stats[m_key]["completed"] += counts["completed"]
            monthly_stats[m_key]["pending"] += counts["pending"]

    global_total = global_total_c + global_total_p
    global_rate = f"{(global_total_c / global_total * 100):.1f}%" if global_total > 0 else "0.0%"

    lines = [
        "# 🌐 Global Task & Productivity Summary\n",
        "> Aggregated analytics across all repositories and client projects.\n",
        "## 🏆 Executive Summary\n",
        f"- **Total Tasks Logged**: `{global_total}`",
        f"- **Total Completed**: `{global_total_c}` (✅)",
        f"- **Total Pending**: `{global_total_p}` (⏳)",
        f"- **Overall Completion Rate**: `{global_rate}`\n",
        "```mermaid",
        "pie title Overall Portfolio Resolution",
        f'    "Completed" : {global_total_c if global_total_c > 0 else 0.001}',
        f'    "Pending" : {global_total_p if global_total_p > 0 else 0.001}',
        "```\n",
        "## 🏢 Project-Wise Breakdown\n",
        "| Project | Total Tasks | Completed | Pending | Completion Rate | Dashboard |",
        "| :--- | :---: | :---: | :---: | :---: | :---: |"
    ]
    
    for ps in project_summary:
        lines.append(f'| **{ps["name"]}** | {ps["total"]} | {ps["completed"]} | {ps["pending"]} | {ps["rate"]} | [View Analytics](./{ps["name"]}/Analytics.md) |')
        
    lines.append("\n## 📅 Multi-Period Performance\n")
    lines.append("### 📆 Daily Aggregates")
    lines.append("| Date | Created | Resolved | Pending | Day Completion |")
    lines.append("| :---: | :---: | :---: | :---: | :---: |")
    for d_str in sorted(daily_stats.keys(), key=lambda x: datetime.strptime(x, "%d-%m-%Y"), reverse=True):
        c = daily_stats[d_str]["completed"]
        p = daily_stats[d_str]["pending"]
        tot = c + p
        rate = f"{(c / tot * 100):.0f}%" if tot > 0 else "0%"
        lines.append(f"| {d_str} | {tot} | {c} | {p} | {rate} |")

    lines.append("\n### 🗓️ Weekly Summary")
    lines.append("| Week | Total Tasks | Resolved | Pending | Weekly Efficiency |")
    lines.append("| :---: | :---: | :---: | :---: | :---: |")
    for w_str in sorted(weekly_stats.keys(), reverse=True):
        c = weekly_stats[w_str]["completed"]
        p = weekly_stats[w_str]["pending"]
        tot = c + p
        rate = f"{(c / tot * 100):.0f}%" if tot > 0 else "0%"
        lines.append(f"| {w_str} | {tot} | {c} | {p} | {rate} |")

    lines.append("\n### 📊 Monthly Overview")
    lines.append("| Month | Total Tasks | Resolved | Pending | Resolution Rate |")
    lines.append("| :---: | :---: | :---: | :---: | :---: |")
    for m_str in sorted(monthly_stats.keys(), reverse=True):
        c = monthly_stats[m_str]["completed"]
        p = monthly_stats[m_str]["pending"]
        tot = c + p
        rate = f"{(c / tot * 100):.0f}%" if tot > 0 else "0%"
        lines.append(f"| {m_str} | {tot} | {c} | {p} | {rate} |")
        
    lines.append("\n---\n*Dashboard auto-updated by GitHub Actions.*")
    return "\n".join(lines)

def update_main_readme(projects):
    lines = [
        "# 📓 MyWorkDairy\n",
        "Personal work tracker for daily queries, solutions, task updates, and project status across all repositories.\n",
        "### 📊 Analytics & Dashboards:",
        "- 🌐 **[Global Summary Dashboard](./Global_Summary.md)** *(Aggregate counts, Daily/Weekly/Monthly views)*\n",
        "### 📁 Project Logs & Individual Analytics:\n"
    ]
    
    for proj_name in sorted(projects.keys()):
        lines.append(f"- 📂 **{proj_name}**:")
        lines.append(f"  - 📝 [Work Log](./{proj_name}/WorkLog.md)")
        lines.append(f"  - 📈 [Task Analytics](./{proj_name}/Analytics.md)")
        
    lines.append("\n---\n*Maintained daily with automated Mermaid analytics.*")
    return "\n".join(lines)

def main():
    projects = parse_worklogs()
    
    # Generate Project Analytics
    for proj_name, data in projects.items():
        analytics_md = generate_project_analytics(proj_name, data)
        analytics_path = os.path.join(BASE_DIR, proj_name, 'Analytics.md')
        with open(analytics_path, 'w', encoding='utf-8') as f:
            f.write(analytics_md)
        print(f"Generated {analytics_path}")
        
    # Generate Global Summary
    global_md = generate_global_summary(projects)
    global_path = os.path.join(BASE_DIR, 'Global_Summary.md')
    with open(global_path, 'w', encoding='utf-8') as f:
        f.write(global_md)
    print(f"Generated {global_path}")
    
    # Update README
    readme_md = update_main_readme(projects)
    readme_path = os.path.join(BASE_DIR, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_md)
    print(f"Updated {readme_path}")

if __name__ == '__main__':
    main()
