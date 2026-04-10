import requests
import os

def run_workflow():
    pat = os.getenv('COZE_PAT')
    workflow_id = os.getenv('COZE_WORKFLOW_ID')
    space_id = os.getenv('COZE_SPACE_ID')

    url = "https://api.coze.com/v1/workflow/run"
    headers = {
        "Authorization": f"Bearer {pat}",
        "Agw-Workspace-Id": space_id,
        "Content-Type": "application/json"
    }
    payload = {
        "workflow_id": workflow_id,
        "parameters": {"USER_INPUT": "执行定时行情分析并发布到币安广场"}
    }

    print(f"🚀 正在调用工作流...")
    response = requests.post(url, headers=headers, json=payload)
    print(f"📥 结果: {response.text}")

if __name__ == "__main__":
    run_workflow()
