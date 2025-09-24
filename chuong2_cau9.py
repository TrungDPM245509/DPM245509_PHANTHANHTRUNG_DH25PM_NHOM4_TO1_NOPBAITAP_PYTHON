'''
Câu 9: Giải thích kết quả tính toán của các biểu thức

Trả lời:

(a) i1 + (i2 * i3)
Tính: 2 + (5 * -3) = 2 + (-15) = -13
Kết quả: -13
Giải thích: Phép nhân 5 * -3 được thực hiện trước, sau đó cộng với 2.

(b) i1 * (i2 + i3)
Tính: 2 * (5 + (-3)) = 2 * 2 = 4
Kết quả: 4
Giải thích: Phép cộng trong ngoặc được thực hiện trước, rồi nhân với 2.

(c) i1 / (i2 + i3)
Tính: 2 / (5 + (-3)) = 2 / 2 = 1.0
Kết quả: 1.0
Giải thích: Phép cộng trong ngoặc là 2, phép chia trong Python 3 trả về float.

(d) i1 // (i2 + i3)
Tính: 2 // (5 + (-3)) = 2 // 2 = 1
Kết quả: 1
Giải thích: Phép chia lấy phần nguyên (//) trả về số nguyên phần nguyên của 2/2.

(e) i1 / i2 + i3
Tính: (2 / 5) + (-3) = 0.4 + (-3) = -2.6
Kết quả: -2.6
Giải thích: Phép chia trước, sau đó cộng.

(f) i1 // i2 + i3
Tính: (2 // 5) + (-3) = 0 + (-3) = -3
Kết quả: -3
Giải thích: 2 // 5 = 0 vì lấy phần nguyên, rồi cộng với -3.

(g) 3 + 4 + 5 / 3
Tính: 3 + 4 + (5 / 3) = 3 + 4 + 1.666666... = 8.666666...
Kết quả: 8.666666666666666
Giải thích: Phép chia có ưu tiên cao hơn phép cộng, nên thực hiện 5 / 3 trước.

(h) 3 + 4 + 5 // 3
Tính: 3 + 4 + (5 // 3) = 3 + 4 + 1 = 8
Kết quả: 8
Giải thích: Phép chia lấy phần nguyên 5 // 3 = 1.

(i) (3 + 4 + 5) / 3
Tính: (3 + 4 + 5) / 3 = 12 / 3 = 4.0
Kết quả: 4.0
Giải thích: Tính tổng trong ngoặc trước, rồi chia.

(j) (3 + 4 + 5) // 3
Tính: 12 // 3 = 4
Kết quả: 4
Giải thích: Chia lấy phần nguyên, kết quả là số nguyên.

(k) d1 + (d2 * d3)
Tính: 2.0 + (5.0 * -0.5) = 2.0 + (-2.5) = -0.5
Kết quả: -0.5
Giải thích: Phép nhân trong ngoặc thực hiện trước.

(l) d1 + d2 * d3
Tính: 2.0 + 5.0 * -0.5 = 2.0 + (-2.5) = -0.5
Kết quả: -0.5
Giải thích: Toán tử nhân có ưu tiên cao hơn cộng, nên nhân trước.

(m) d1 / d2 - d3
Tính: 2.0 / 5.0 - (-0.5) = 0.4 + 0.5 = 0.9
Kết quả: 0.9
Giải thích: Phép chia và trừ âm (trừ số âm = cộng số dương).

(n) d1 / (d2 - d3)
Tính: 2.0 / (5.0 - (-0.5)) = 2.0 / 5.5 ≈ 0.36363636363636365
Kết quả: Khoảng 0.36363636363636365
Giải thích: Tính trong ngoặc trước, rồi chia.

(o) d1 + d2 + d3 / 3
Tính: 2.0 + 5.0 + (-0.5) / 3 = 2.0 + 5.0 + (-0.16666666666666666) = 6.833333333333334
Kết quả: Khoảng 6.833333333333334
Giải thích: Phép chia được thực hiện trước, rồi cộng dần.

(p) (d1 + d2 + d3) / 3
Tính: (2.0 + 5.0 + (-0.5)) / 3 = 6.5 / 3 ≈ 2.1666666666666665
Kết quả: Khoảng 2.1666666666666665
Giải thích: Tính tổng trong ngoặc, rồi chia.

(q) d1 + d2 + (d3 / 3)
Tính: 2.0 + 5.0 + (-0.5 / 3) = 2.0 + 5.0 + (-0.16666666666666666) = 6.833333333333334
Kết quả: Khoảng 6.833333333333334
Giải thích: Tương tự như (o), nhưng nhấn mạnh thứ tự thực hiện.

(r) 3 * (d1 + d2) * (d1 - d3)
Tính:
Tính trong ngoặc trước:
d1 + d2 = 2.0 + 5.0 = 7.0
d1 - d3 = 2.0 - (-0.5) = 2.0 + 0.5 = 2.5
Nhân các kết quả:
3 * 7.0 * 2.5 = 21.0 * 2.5 = 52.5
Kết quả: 52.5
Giải thích: Tính từng ngoặc trước, sau đó nhân lần lượt.

'''