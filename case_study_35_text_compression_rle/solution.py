# Case Study 35: Text Compression Using Character Runs
# Student Roll Number: 26000639
# Syllabus used: variables, data types, operators, conditionals, loops, strings, lists, tuples, unpacking

print("=" * 72)
print("TEXT COMPRESSION USING CHARACTER RUNS (RUN-LENGTH ENCODING)")
print("=" * 72)

n = int(input("Enter number of strings to compress: "))
samples = []
for i in range(n):
    s = input("Enter string " + str(i + 1) + ": ")
    samples.append(s)

results = []
for text in samples:
    orig_len = len(text)
    if orig_len == 0:
        encoded = ""
        enc_len = 0
        verdict = "EMPTY STRING (Nothing to compress)"
        savings_pct = 0.0
    else:
        encoded = ""
        current_char = text[0]
        run_count = 1
        for i in range(1, orig_len):
            if text[i] == current_char:
                run_count = run_count + 1
            else:
                encoded = encoded + current_char + str(run_count)
                current_char = text[i]
                run_count = 1
        encoded = encoded + current_char + str(run_count)
        enc_len = len(encoded)
        savings_pct = ((orig_len - enc_len) / orig_len) * 100.0

        if enc_len < orig_len:
            verdict = "BENEFICIAL (Saved " + str(orig_len - enc_len) + " chars)"
        elif enc_len == orig_len:
            verdict = "NEUTRAL (Same length)"
        else:
            verdict = "NOT BENEFICIAL (Expanded by " + str(enc_len - orig_len) + " chars; keep original)"

    results.append((text, orig_len, encoded, enc_len, round(savings_pct, 2), verdict))

print("\n" + "=" * 72)
print("COMPRESSION COMPARISON REPORT")
print("=" * 72)
for idx in range(len(results)):
    orig, o_len, enc, e_len, pct, verdict = results[idx]
    print(f"\nSample #{idx + 1}")
    print(f"  Original String : '{orig}' (Length: {o_len})")
    print(f"  Encoded String  : '{enc}' (Length: {e_len})")
    print(f"  Space Change    : {pct:.2f}%")
    print(f"  Assessment      : {verdict}")
