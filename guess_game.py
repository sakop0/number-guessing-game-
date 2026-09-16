"""
لعبة تخمين الرقم (Guess the Number)
====================================
لعبة بسيطة: الحاسوب يختار رقم عشوائي، وأنت تحاول تخمنه.
كل مرة تخمن، اللعبة تقولك إذا رقمك أكبر أو أصغر من الرقم الصحيح.

مشروع تعليمي أول بلغة Python.
"""

import random


def play_game():
    print("=" * 40)
    print(" مرحباً بك بلعبة تخمين الرقم!")
    print("=" * 40)
  
     # البرنامج يختار رقم عشوائي بين 1 و 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7  # عدد المحاولات المسموحة

    print(f"\nفكرت برقم بين 1 و 100. عندك {max_attempts} محاولات تخمنه!\n")

    while attempts < max_attempts:
        try:
            guess = int(input("خمن الرقم: "))
        except ValueError:
            print("⚠️  الرجاء إدخال رقم صحيح فقط.\n")
            continue

        attempts += 1

        if guess < secret_number:
            print(f"⬆️  الرقم أكبر من {guess}! حاول مرة ثانية.")
            print(f"   عدد المحاولات المتبقية: {max_attempts - attempts}\n")
        elif guess > secret_number:
            print(f"⬇️  الرقم أصغر من {guess}! حاول مرة ثانية.")
            print(f"   عدد المحاولات المتبقية: {max_attempts - attempts}\n")
        else:
            print(f"\n🎉 مبروك! خمنت الرقم الصحيح ({secret_number}) خلال {attempts} محاولة!")
            break
    else:
        # لو خلصت المحاولات بدون ما يخمن
        print(f"\n خلصت المحاولات! الرقم الصحيح كان: {secret_number}")

    print("\nشكراً للعب! ")


if __name__ == "__main__":
    play_game()
