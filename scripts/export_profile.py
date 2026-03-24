#!/usr/bin/env python3
"""
员工画像导出脚本
将访谈分析中的员工画像提取并导出为独立文件
"""

import json
import os
from typing import Dict, Optional


class ProfileExporter:
    """员工画像导出器"""
    
    def __init__(self, output_dir: str = "."):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def export_to_markdown(self, 
                          profile_data: Dict, 
                          interviewee_name: str) -> str:
        """
        将员工画像导出为 Markdown 文件
        
        Args:
            profile_data: 员工画像数据
            interviewee_name: 被访谈者姓名
        
        Returns:
            导出的文件路径
        """
        md_content = self._generate_markdown_content(profile_data, interviewee_name)
        filename = f"{interviewee_name}-员工画像.md"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        return filepath
    
    def _generate_markdown_content(self, profile_data: Dict, name: str) -> str:
        """生成 Markdown 内容"""
        
        # 基础信息
        basic_info = profile_data.get("basic_info", {})
        
        content = f"""# {name} - 员工画像补充材料

> 本画像基于访谈内容生成,用于补充员工档案

---

## 📋 基础信息

| 维度 | 内容 |
|------|------|
| **姓名** | {name} |
| **职位** | {basic_info.get("position", "未知")} |
| **职级** | {basic_info.get("level", "未知")} |
| **司龄** | {basic_info.get("tenure", "未知")} |
| **部门** | {basic_info.get("department", "未知")} |

---

## 💪 能力特征画像

### 专业能力
"""
        
        # 专业能力
        professional = profile_data.get("professional_skills", [])
        for skill in professional:
            content += f"\n- **{skill.get('name', '')}**: {skill.get('score', '')} - 证据: \"{skill.get('evidence', '')}\"\n"
        
        content += "\n### 软技能\n"
        soft_skills = profile_data.get("soft_skills", [])
        for skill in soft_skills:
            content += f"- **{skill.get('name', '')}**: {skill.get('description', '')} - 表现: \"{skill.get('evidence', '')}\"\n"
        
        # 职业锚与价值观
        content += "\n### 职业锚与价值观\n"
        content += f"- **职业锚类型**: {profile_data.get('career_anchor', '未识别')}\n"
        
        values = profile_data.get("core_values", [])
        if values:
            content += f"- **核心价值观**: {', '.join(values)}\n"
        
        content += f"- **工作动机**: {profile_data.get('work_motivation', '未明确')}\n"
        
        # AI 素养
        content += "\n### AI 素养\n"
        ai_skills = profile_data.get("ai_skills", {})
        content += f"- **AI工具使用**: {ai_skills.get('usage_level', '未评估')} - {ai_skills.get('tools', '')}\n"
        content += f"- **人机协作**: {ai_skills.get('collaboration_level', '未评估')}\n"
        content += f"- **AI时代适应性**: {ai_skills.get('adaptability', '未评估')}\n"
        
        # 性格与行为模式
        content += "\n## 🎭 性格与行为模式\n"
        personality = profile_data.get("personality", {})
        content += f"- **性格特点**: {personality.get('traits', '')} - 行为证据: \"{personality.get('evidence', '')}\"\n"
        content += f"- **沟通风格**: {personality.get('communication_style', '')} - 典型表达: \"{personality.get('example', '')}\"\n"
        content += f"- **决策方式**: {personality.get('decision_style', '')} - 示例: \"{personality.get('example', '')}\"\n"
        content += f"- **压力反应**: {personality.get('stress_response', '')} - 情境: \"{personality.get('example', '')}\"\n"
        
        # 战场画像
        battlefield = profile_data.get("battlefield", {})
        if battlefield:
            content += "\n## ⚔️ 战场画像\n"
            
            current_work = battlefield.get("current_work", {})
            if current_work:
                content += "\n### 当前\"战场\"描述\n"
                content += "**核心工作内容:**\n"
                for work in current_work.get("areas", []):
                    content += f"- {work.get('name', '')}: {work.get('description', '')}\n"
                
                challenges = current_work.get("challenges", [])
                if challenges:
                    content += "\n**关键挑战:**\n"
                    for challenge in challenges:
                        content += f"- {challenge.get('name', '')}: {challenge.get('description', '')}\n"
                
                content += f"\n**工作环境:** {current_work.get('environment', '')}\n"
                content += f"\n**战场特征:**\n"
                features = current_work.get("features", {})
                content += f"- 复杂度: {features.get('complexity', '')}\n"
                content += f"- 不确定性: {features.get('uncertainty', '')}\n"
                content += f"- 压力水平: {features.get('pressure', '')}\n"
                content += f"- 技术前沿性: {features.get('tech_frontier', '')}\n"
            
            performance = battlefield.get("performance", {})
            if performance:
                content += "\n### 当前\"战场\"表现(自我感知)\n"
                
                achievements = performance.get("achievements", [])
                if achievements:
                    content += "**工作成果:**\n"
                    for achievement in achievements:
                        content += f"- {achievement.get('name', '')}: {achievement.get('description', '')} - 证据: \"{achievement.get('evidence', '')}\"\n"
                
                content += f"\n**自我评估:**\n"
                content += f"- 工作满意度: {performance.get('satisfaction', '')}\n"
                content += f"- 能力发挥度: {performance.get('ability_utilization', '')}\n"
                content += f"- 成就感来源: {performance.get('achievement_source', '')}\n"
                
                difficulties = performance.get("difficulties", [])
                if difficulties:
                    content += "\n**遇到的困难:**\n"
                    for difficulty in difficulties:
                        content += f"- {difficulty.get('name', '')}: {difficulty.get('description', '')} - 应对方式: \"{difficulty.get('response', '')}\"\n"
                
                advantages = performance.get("advantages", [])
                if advantages:
                    content += "\n**优势领域:**\n"
                    for advantage in advantages:
                        content += f"- {advantage.get('name', '')}: {advantage.get('description', '')} - 表现: \"{advantage.get('evidence', '')}\"\n"
            
            plans = battlefield.get("plans", {})
            if plans:
                content += "\n### 后续工作计划\n"
                
                short_term = plans.get("short_term", [])
                if short_term:
                    content += "**短期计划(1-3个月):**\n"
                    for plan in short_term:
                        content += f"- {plan.get('name', '')}: {plan.get('action', '')}\n"
                
                medium_term = plans.get("medium_term", [])
                if medium_term:
                    content += "\n**中期计划(3-6个月):**\n"
                    for plan in medium_term:
                        content += f"- {plan.get('name', '')}: {plan.get('goal', '')}\n"
                
                long_term = plans.get("long_term", [])
                if long_term:
                    content += "\n**长期展望(6个月以上):**\n"
                    for plan in long_term:
                        content += f"- {plan.get('name', '')}: {plan.get('direction', '')}\n"
                
                improvements = plans.get("improvements", [])
                if improvements:
                    content += "\n**能力提升需求:**\n"
                    for improvement in improvements:
                        content += f"- {improvement.get('name', '')}: {improvement.get('plan', '')}\n"
                
                support = plans.get("support", [])
                if support:
                    content += "\n**支持需求:**\n"
                    for item in support:
                        content += f"- {item.get('name', '')}: {item.get('content', '')}\n"
        
        # 发展潜力与风险
        content += "\n## 🚀 发展潜力与风险\n"
        
        potential = profile_data.get("potential", {})
        if potential:
            advantages = potential.get("advantages", [])
            if advantages:
                content += "### 发展潜力\n"
                for advantage in advantages:
                    content += f"- **{advantage.get('name', '')}**: {advantage.get('description', '')} - 发展建议: \"{advantage.get('suggestion', '')}\"\n"
            
            growth = potential.get("growth", [])
            if growth:
                content += "\n**成长空间:**\n"
                for item in growth:
                    content += f"- {item.get('name', '')}: {item.get('description', '')} - 提升路径: \"{item.get('path', '')}\"\n"
        
        risks = profile_data.get("risks", [])
        if risks:
            content += "\n### 潜在风险\n"
            for risk in risks:
                content += f"- **{risk.get('name', '')}**: {risk.get('description', '')} - 信号: \"{risk.get('signal', '')}\"\n"
        
        # 补充说明
        content += f"""
---

## 📝 补充说明

- 本画像基于访谈内容生成,反映了被访谈者在特定时间点的工作状态和认知
- 建议结合其他评估工具和绩效数据进行综合判断
- 画像数据可用于员工发展计划制定、岗位匹配评估等场景

---

*生成时间: {profile_data.get('generated_at', '')}*
*数据来源: 访谈分析*
"""
        
        return content


def export_profile(profile_data: Dict, name: str, output_dir: str = ".") -> str:
    """
    导出员工画像
    
    Args:
        profile_data: 画像数据
        name: 被访谈者姓名
        output_dir: 输出目录
    
    Returns:
        导出文件的路径
    """
    exporter = ProfileExporter(output_dir)
    return exporter.export_to_markdown(profile_data, name)


if __name__ == "__main__":
    # 测试示例
    test_profile = {
        "basic_info": {
            "position": "前端开发工程师",
            "level": "T8",
            "tenure": "2年3个月",
            "department": "QQ业务线"
        },
        "professional_skills": [
            {"name": "前端开发", "score": "⭐⭐⭐⭐⭐", "evidence": "使用CodeBuddy完成平台demo"},
            {"name": "AI工具使用", "score": "⭐⭐⭐⭐⭐", "evidence": "日均高频使用CodeBuddy"}
        ],
        "soft_skills": [
            {"name": "创新意识", "description": "强", "evidence": "主动探索新工具"}
        ],
        "career_anchor": "技术/职能型",
        "core_values": ["技术创新", "效率提升"],
        "work_motivation": "通过技术解决实际问题",
        "ai_skills": {
            "usage_level": "广泛",
            "tools": "CodeBuddy、内部AI平台",
            "collaboration_level": "成熟",
            "adaptability": "强"
        },
        "personality": {
            "traits": "积极主动、创新性强",
            "evidence": "30分钟完成1周工作",
            "communication_style": "直接高效",
            "example": "表达清晰明确",
            "decision_style": "数据驱动",
            "example": "基于提效数据决策",
            "stress_response": "抗压能力强",
            "example": "面对挑战保持冷静"
        },
        "battlefield": {
            "current_work": {
                "areas": [
                    {"name": "AI平台开发", "description": "负责AI相关功能开发"}
                ],
                "challenges": [
                    {"name": "资源限制", "description": "外部模型调用受限"}
                ],
                "environment": "技术创新团队",
                "features": {
                    "complexity": "高",
                    "uncertainty": "中",
                    "pressure": "中",
                    "tech_frontier": "高"
                }
            }
        },
        "potential": {
            "advantages": [
                {"name": "AI工具掌握", "description": "熟练掌握AI工具", "suggestion": "可担任AI导师"}
            ]
        },
        "risks": [
            {"name": "团队协作", "description": "个人memory难以共享", "signal": "多AI上下文不同步"}
        ],
        "generated_at": "2026-03-24"
    }
    
    filepath = export_profile(test_profile, "翁行", output_dir=".")
    print(f"导出文件: {filepath}")
