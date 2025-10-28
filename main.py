#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gemini 2.5 Flash Lite API サンプル

APIレスポンスの形式:
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "生成されたテキストがここに入ります..."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 8,
    "candidatesTokenCount": 566,
    "totalTokenCount": 574,
    "promptTokensDetails": [
      {
        "modality": "TEXT",
        "tokenCount": 8
      }
    ]
  },
  "modelVersion": "gemini-2.5-flash-lite",
  "responseId": "一意のレスポンスID"
}
"""

import requests
import json
import sys
import io

# 標準出力のエンコーディングをUTF-8に設定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Gemini 2.5 Flash Lite API設定(https://aistudio.google.com/api-keys)
API_KEY = "<APIキー>"
MODEL_NAME = "gemini-2.5-flash-lite"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"

def main():
    # リクエストヘッダー
    headers = {
        "x-goog-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    # リクエストボディ
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "こんにちは！AIについて簡単に説明してください。"
                    }
                ]
            }
        ]
    }

    # APIリクエスト送信
    print("Gemini 2.5 Flash Lite APIにリクエストを送信中...")
    response = requests.post(API_URL, headers=headers, json=data)

    # レスポンスの処理
    if response.status_code == 200:
        result = response.json()

        # 結果を見やすく表示
        print("\n" + "="*60)
        print("APIレスポンス:")
        print("="*60)

        # テキスト部分のみ抽出して表示
        if "candidates" in result and len(result["candidates"]) > 0:
            text_content = result["candidates"][0]["content"]["parts"][0]["text"]
            print(text_content)

        print("\n" + "="*60)
        print("完全なレスポンス (JSON):")
        print("="*60)
        print(json.dumps(result, indent=2, ensure_ascii=False))

    else:
        print(f"\nエラー: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    main()
