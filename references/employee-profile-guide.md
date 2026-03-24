# 👤 员工画像自动生成指南

本文档说明如何基于访谈内容自动生成员工画像。

## 📋 画像结构

### 1. 基础画像信息

| 维度 | 数据来源 | 示例 |
|------|---------|------|
| **姓名** | 访谈记录/元数据 | 陈晴 |
| **职位** | 访谈记录/元数据 | 产品经理 |
| **职级** | 访谈记录/元数据 | T8 |
| **司龄** | 访谈记录/元数据 | 3年6月 |
| **部门** | 访谈记录/元数据 | 频道产品部 |

---

### 2. 能力特征画像

#### 2.1 专业能力

**提取维度：**
- 专业知识储备
- 技术技能
- 行业经验
- 项目管理能力
- 产品思维能力

**评估方法：**
```python
def extract_professional_skills(interview_text):
    """
    从访谈中提取专业能力信息
    """
    skills = {
        "产品思维": {
            "score": 4.8,  # 1-5分
            "evidence": [
                "用户提到：'我在做频道AI Agent的时候，会从用户场景出发，不是从技术出发'",
                "用户强调：'洞察力和判断力很难被AI取代'"
            ]
        },
        "AI应用能力": {
            "score": 5.0,
            "evidence": [
                "熟练使用 Manus、CodeBard、Cursor、豆包、Gemini 等多种AI工具",
                "主导频道AI Agent项目，实现15个频道试点"
            ]
        },
        "项目管理": {
            "score": 4.2,
            "evidence": [
                "主导多个产品项目",
                "能够协调跨团队资源"
            ]
        }
    }
    return skills
```

**输出格式：**
```markdown
#### 专业能力
- **产品思维**：⭐⭐⭐⭐⭐ (4.8/5)
  - 证据："我在做频道AI Agent的时候，会从用户场景出发"
  - 证据："洞察力和判断力很难被AI取代"

- **AI应用能力**：⭐⭐⭐⭐⭐ (5.0/5)
  - 证据：熟练使用 Manus、CodeBard、Cursor 等多种AI工具
  - 证据：主导频道AI Agent项目，实现15个频道试点

- **项目管理**：⭐⭐⭐⭐ (4.2/5)
  - 证据：主导多个产品项目
  - 证据：能够协调跨团队资源
```

---

#### 2.2 软技能

**提取维度：**
- 沟通能力
- 团队协作
- 领导力
- 学习能力
- 创新能力

**评估示例：**
```python
soft_skills = {
    "沟通能力": {
        "level": "强",
        "evidence": "表达清晰，逻辑性强"
    },
    "团队协作": {
        "level": "良好",
        "evidence": "在小团队内协作良好，但跨团队协作成本高"
    },
    "学习能力": {
        "level": "极强",
        "evidence": "快速掌握多种AI工具，并应用于实际项目"
    }
}
```

---

### 3. 职业锚与价值观

#### 3.1 职业锚识别

**8种职业锚类型：**

| 职业锚 | 核心特征 | 识别信号 |
|--------|---------|---------|
| **技术/职能型** | 追求专业精进 | 强调技术深度、不愿做管理 |
| **管理型** | 追求管理责任 | 关注团队规模、喜欢决策 |
| **自主/独立型** | 追求工作自由 | 不喜欢约束、追求灵活性 |
| **安全/稳定型** | 追求稳定可预测 | 关注稳定性、厌恶变化 |
| **创业/创造型** | 追求创造新事物 | 喜欢从0到1、不满足于守成 |
| **服务/奉献型** | 追求帮助他人 | 强调社会价值、关心团队成长 |
| **纯挑战型** | 追求战胜难题 | 喜欢高难度、竞争导向 |
| **生活方式型** | 追求工作生活平衡 | 关注WLB、抵触加班 |

**识别算法：**
```python
def identify_career_anchor(interview_text):
    """
    识别员工的职业锚类型
    """
    anchors = {
        "技术/职能型": 0,
        "管理型": 0,
        "自主/独立型": 0,
        "安全/稳定型": 0,
        "创业/创造型": 0,
        "服务/奉献型": 0,
        "纯挑战型": 0,
        "生活方式型": 0
    }
    
    # 基于关键词匹配
    if "技术深度" in interview_text or "专业" in interview_text:
        anchors["技术/职能型"] += 3
    
    if "团队" in interview_text or "决策" in interview_text:
        anchors["管理型"] += 2
    
    if "灵活" in interview_text or "自由" in interview_text:
        anchors["自主/独立型"] += 3
    
    # ... 其他职业锚的识别逻辑
    
    # 返回得分最高的职业锚
    primary_anchor = max(anchors, key=anchors.get)
    return primary_anchor
```

**输出格式：**
```markdown
#### 职业锚与价值观
- **职业锚类型**：技术/职能型 + 自主/独立型（复合型）
  - 信号：强调技术深度、不愿意做纯管理
  - 信号：喜欢灵活的工作方式，抵触僵化流程
  
- **核心价值观**
  - 🎯 用户导向："从用户场景出发，不是从技术出发"
  - 🚀 创新：喜欢尝试新技术、新方法
  - ⚡ 效率：强调快速迭代，反对流程冗长
  
- **工作动机**
  - 技术成就感：通过技术创新解决问题
  - 用户价值：为用户创造价值是核心驱动力
  - 学习成长：持续学习新技术、新方法
```

---

### 4. AI 素养评估（v2.1 新增）

**评估维度：**

| 维度 | 评估标准 | 证据提取 |
|------|---------|---------|
| **AI工具使用** | 广度（工具种类）+ 深度（应用水平） | 提及的AI工具清单、使用频率 |
| **人机协作** | 协作成熟度、工作模式 | "AI+人"的工作流描述 |
| **AI时代适应性** | 对AI影响的认知、适应能力 | 对岗位演变的理解、能力更新行动 |

**评估示例：**
```python
ai_literacy = {
    "工具使用": {
        "level": "广泛且深入",
        "tools": [
            "Manus（产品设计）",
            "CodeBard（代码生成）",
            "Cursor（编程助手）",
            "豆包（通用AI）",
            "Gemini（多模态）",
            "小龙虾（数据分析）",
            "AI Studio（模型微调）",
            "Leonardo.ai（图像生成）"
        ],
        "score": 5.0
    },
    "人机协作": {
        "level": "成熟",
        "workflow": "AI辅助设计 + 人工决策 + AI执行",
        "score": 4.5
    },
    "AI时代适应性": {
        "level": "高",
        "understanding": "理解AI对岗位的影响，主动适应变化",
        "actions": [
            "主导AI Agent产品项目",
            "持续学习新AI工具",
            "思考AI时代的职业发展"
        ],
        "score": 4.8
    }
}
```

**输出格式：**
```markdown
#### AI 素养
- **AI工具使用**：⭐⭐⭐⭐⭐ (5.0/5)
  - 广度：使用8种以上AI工具
  - 深度：熟练应用于实际项目
  - 工具清单：Manus、CodeBard、Cursor、豆包、Gemini、小龙虾、AI Studio、Leonardo.ai

- **人机协作**：⭐⭐⭐⭐⭐ (4.5/5)
  - 协作模式：AI辅助设计 + 人工决策 + AI执行
  - 协作成熟度：能够有效利用AI提升效率

- **AI时代适应性**：⭐⭐⭐⭐⭐ (4.8/5)
  - 岗位认知：理解AI对产品经理岗位的影响
  - 适应行动：主导AI Agent产品项目，持续学习新AI工具
```

---

### 5. 性格与行为模式

**提取维度：**
- 性格特点
- 沟通风格
- 决策方式
- 压力反应

**提取方法：**
```python
def extract_personality_patterns(interview_text):
    """
    提取性格和行为模式
    """
    patterns = {
        "性格特点": {
            "trait": "积极主动、善于思考",
            "evidence": [
                "用户主动尝试新AI工具",
                "对AI产品化有深度思考"
            ]
        },
        "沟通风格": {
            "style": "逻辑清晰、有洞察力",
            "evidence": [
                "表达层次分明",
                "善于提炼核心观点"
            ]
        },
        "决策方式": {
            "method": "数据驱动 + 直觉判断",
            "evidence": [
                "重视AI工具的效率提升",
                "强调洞察力和判断力的重要性"
            ]
        },
        "压力反应": {
            "pattern": "主动寻求解决方案",
            "evidence": [
                "面对流程冗长，提出小团队FT模式的解决方案"
            ]
        }
    }
    return patterns
```

---

### 6. 发展潜力与风险

#### 6.1 发展潜力

**识别维度：**
- 优势领域
- 成长空间
- 发展路径

**示例：**
```python
development_potential = {
    "优势领域": [
        {
            "area": "AI产品化",
            "strength": "深度理解AI产品化的难点和不确定性",
            "suggestion": "可成为AI产品专家，推动组织AI产品标准建立"
        }
    ],
    "成长空间": [
        {
            "area": "跨团队协作",
            "current_level": "中等",
            "target": "提升跨团队影响力",
            "path": "主导跨团队项目，建立协作网络"
        }
    ]
}
```

#### 6.2 潜在风险

**识别维度：**
- 风险点
- 风险信号
- 应对建议

**示例：**
```python
potential_risks = [
    {
        "risk": "过度依赖AI工具",
        "signal": "用户提到'用了AI之后变得更累了'",
        "suggestion": "注意平衡AI工具使用和人工判断，避免能力退化"
    },
    {
        "risk": "对流程的抵触情绪",
        "signal": "用户多次批评流程冗长",
        "suggestion": "引导用户理解流程的价值，同时优化流程效率"
    }
]
```

---

## 📤 画像导出选项

### 1. 导出为 Markdown 文件

**格式：**
```markdown
# 员工画像 - [姓名]

## 基础信息
- 姓名：[姓名]
- 职位：[职位]
- 职级：[职级]
- 司龄：[司龄]
- 部门：[部门]

## 能力特征
...

## 职业锚与价值观
...

## AI 素养
...

## 性格与行为模式
...

## 发展潜力与风险
...

---
生成时间：[YYYY-MM-DD HH:MM]
生成工具：Employee Interview Analyzer v2.1.0
```

### 2. 创建为腾讯文档

**流程：**
```python
def export_to_tencent_docs(profile_data):
    """
    将员工画像导出为腾讯文档
    """
    from tencent_docs_mcp import create_smartcanvas_by_markdown
    
    markdown_content = generate_markdown_profile(profile_data)
    
    doc = create_smartcanvas_by_markdown(
        title=f"员工画像 - {profile_data['name']}",
        markdown=markdown_content
    )
    
    return doc['url']
```

**使用场景：**
- 团队协作时，便于实时查看和更新
- 与HR系统集成，实现画像数据同步
- 分享给相关人员，便于团队协作

### 3. 补充到员工档案系统

**流程：**
```python
def sync_to_hr_system(profile_data):
    """
    同步员工画像到HR系统
    """
    hr_system_api.update_employee_profile(
        employee_id=profile_data['employee_id'],
        profile_data={
            'skills': profile_data['skills'],
            'career_anchor': profile_data['career_anchor'],
            'ai_literacy': profile_data['ai_literacy'],
            'personality': profile_data['personality'],
            'potential': profile_data['potential'],
            'risks': profile_data['risks']
        }
    )
```

---

## 💡 生成流程

### 1. 分析完成后提示用户

```
👤 员工画像导出选项：
"已生成员工画像，是否需要导出？
  1️⃣ 导出为 Markdown 文件
  2️⃣ 创建为腾讯文档（便于团队协作）
  3️⃣ 补充到员工档案系统
  4️⃣ 暂不需要"

如果选择导出，进一步询问：
"请选择导出目的：
  1️⃣ 补充员工档案
  2️⃣ 团队分析
  3️⃣ 其他"
```

### 2. 提取画像数据

基于访谈内容，使用自然语言处理技术提取各类画像信息。

### 3. 生成画像文档

根据选择的格式（MD/腾讯文档），生成对应的画像文档。

### 4. 导出或同步

根据用户选择，导出文件、创建腾讯文档或同步到HR系统。

---

## 📝 使用建议

1. **画像验证**：在导出前，让员工确认画像的准确性
2. **定期更新**：建议每季度或每半年更新一次员工画像
3. **多源数据**：结合绩效评估、360反馈等多源数据丰富画像
4. **隐私保护**：注意保护员工隐私，仅分享给授权人员

---

## 🔧 技术实现

**依赖工具：**
- 自然语言处理：提取关键信息
- 知识图谱：构建员工画像图谱
- 数据可视化：生成画像雷达图
- 腾讯文档MCP：创建和导出腾讯文档

**数据结构：**
```json
{
  "basic_info": {
    "name": "陈晴",
    "position": "产品经理",
    "level": "T8",
    "tenure": "3年6月",
    "department": "频道产品部"
  },
  "skills": {
    "professional": {...},
    "soft": {...}
  },
  "career_anchor": {
    "type": "技术/职能型",
    "values": [...]
  },
  "ai_literacy": {...},
  "personality": {...},
  "potential": {...},
  "risks": [...]
}
```
