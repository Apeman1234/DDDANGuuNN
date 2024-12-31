import json

# 위의 JSON을 변수로 저장
data = {
    "이미지코드": {
        "최아린": ["zmmducI", "WRWrsjb", "KcjYHZb", "qU8NFs8", "B24lChV", "dt0GGC", "RwMbmQi", "4FBU6Jf", "cFo7Q6P", "xcVG3Ji"],
        "정수연": ["sltcfAa", "ZgxnvUt", "FxczXhh", "oJjKatD", "p98C1wU", "Jfp9bp9", "MnErBtT", "uYyK1A2", "Tdk8C1e", "lX7t91u"],
        "박하린": ["PoRL7Gz", "7BrPWwC", "QuYZaLm", "xc4DSTi", "Faial4q", "AEYpRSE", "fp6RxG6", "IFU4Tfi", "o4ag7wm", "BefFnSG"],
        "이은희": ["fZ52qqv", "4st92zN", "ydfKjbj", "Ph73gQc", "rsJn9ie", "m7c7HJl", "3pAEsiE", "jFUU9dw", "eIM7LXa", "xLuNEtG"],
        "나미래": ["9619mxl", "1OlxXKp", "Bfrfag4", "tJqrLdh", "oO0pwYz", "CyREpoN", "6JivApZ", "9A9ZBUi", "tktZTqX", "FxQLbIj"],
        "김나리": ["lM1KvFZ", "lH4F6aE", "rkRGCWf", "wWeLPZD", "AFVm7Ro", "mOxGLWk", "hfnoF0W", "R7K5a6z", "wQuyBVZ", "XoNg1lp"],
        "홍세희": ["fDp2Qyi", "xnl4zBH", "TQK4In0", "eeATBAJ", "PmViMZI", "UimanRe", "nkyMpUK", "6p7y5Wv", "HGvekZX", "QzoFD1B"],
        "오지혜": ["f0tksGl", "pbYKE6Y", "hlt61Ui", "jjh4637", "Dc0WfuF", "Dfpqkpz", "J8GkJNx", "Tn9v933", "A4D3BYQ", "cHd2d9A"],
        "황소연": ["XzFSFmq", "jAIExfG", "Rqg7Wr1", "ACQR6Rv", "LVJJHlE", "fYh1I8X", "znqwe0B", "WWrNCi6", "k6EuSof", "4w0ykcx"],
        "장하윤": ["i7Zl7Gx", "QEJHFjS", "PHNjflM", "ljOatkn", "t5osI78", "5HkqRhX", "jpnyLVX", "CcmyTJZ", "HuxcRAC", "mWu6acQ"]
    }
}

# '최아린' 캐릭터의 첫 번째 이미지 코드 가져오기
image_code_for_arin = data["이미지코드"]["최아린"][0]
print(f"최아린의 첫 번째 이미지 코드: {image_code_for_arin}")