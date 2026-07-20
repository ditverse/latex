def compute_lps(pattern):
    lps = [0] * len(pattern)
    prefix_len = 0
    index = 1

    while index < len(pattern):
        if pattern[index] == pattern[prefix_len]:
            prefix_len += 1
            lps[index] = prefix_len
            index += 1
        elif prefix_len != 0:
            prefix_len = lps[prefix_len - 1]
        else:
            lps[index] = 0
            index += 1

    return lps


def kmp_match(text, pattern):
    if pattern == "":
        return {"index": 0, "lps": [], "trace": ["Pola kosong ditemukan di indeks 0."]}

    lps = compute_lps(pattern)
    text_index = 0
    pattern_index = 0
    trace = []

    while text_index < len(text):
        trace.append(
            f"Bandingkan text[{text_index}]='{text[text_index]}' "
            f"dengan pattern[{pattern_index}]='{pattern[pattern_index]}'"
        )

        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1

            if pattern_index == len(pattern):
                start_index = text_index - pattern_index
                trace.append(f"Pola ditemukan mulai indeks {start_index}.")
                return {"index": start_index, "lps": lps, "trace": trace}
        elif pattern_index != 0:
            pattern_index = lps[pattern_index - 1]
            trace.append(f"Tidak cocok, geser pola ke indeks pattern {pattern_index}.")
        else:
            text_index += 1
            trace.append("Tidak cocok, lanjut ke karakter teks berikutnya.")

    return {"index": -1, "lps": lps, "trace": trace}


def build_last_occurrence(pattern):
    last = {}
    for index, char in enumerate(pattern):
        last[char] = index
    return last


def boyer_moore_match(text, pattern):
    if pattern == "":
        return {
            "index": 0,
            "last_occurrence": {},
            "trace": ["Pola kosong ditemukan di indeks 0."],
        }

    last = build_last_occurrence(pattern)
    text_len = len(text)
    pattern_len = len(pattern)
    start = 0
    trace = []

    while start <= text_len - pattern_len:
        pattern_index = pattern_len - 1

        while (
            pattern_index >= 0
            and pattern[pattern_index] == text[start + pattern_index]
        ):
            trace.append(
                f"Shift {start}: cocok pattern[{pattern_index}] "
                f"dengan text[{start + pattern_index}]"
            )
            pattern_index -= 1

        if pattern_index < 0:
            trace.append(f"Pola ditemukan mulai indeks {start}.")
            return {"index": start, "last_occurrence": last, "trace": trace}

        mismatch_char = text[start + pattern_index]
        last_index = last.get(mismatch_char, -1)
        shift = max(1, pattern_index - last_index)
        trace.append(
            f"Shift {start}: tidak cocok pada '{mismatch_char}', "
            f"geser {shift} posisi."
        )
        start += shift

    return {"index": -1, "last_occurrence": last, "trace": trace}


def format_match(text, pattern, index):
    if index < 0:
        return "Pola tidak ditemukan."

    pointer = " " * index + "^" * len(pattern)
    return f"{text}\n{pointer}\n{pattern} ditemukan mulai indeks {index}."


def run_case(text, pattern):
    kmp_result = kmp_match(text, pattern)
    bm_result = boyer_moore_match(text, pattern)

    print("Kasus pencocokan string")
    print(f"Text    : {text}")
    print(f"Pattern : {pattern}")
    print()

    print("KMP")
    print(f"LPS/failure table : {kmp_result['lps']}")
    print(f"Indeks ditemukan : {kmp_result['index']}")
    print(format_match(text, pattern, kmp_result["index"]))
    print("Trace ringkas:")
    for step in kmp_result["trace"][:12]:
        print(step)
    if len(kmp_result["trace"]) > 12:
        print("...")
    print()

    print("Boyer-Moore")
    print(f"Last occurrence table : {bm_result['last_occurrence']}")
    print(f"Indeks ditemukan : {bm_result['index']}")
    print(format_match(text, pattern, bm_result["index"]))
    print("Trace ringkas:")
    for step in bm_result["trace"][:12]:
        print(step)
    if len(bm_result["trace"]) > 12:
        print("...")


if __name__ == "__main__":
    ptext = "abacaabacabacababa"
    pattern = "acabaca"
    run_case(ptext, pattern)
