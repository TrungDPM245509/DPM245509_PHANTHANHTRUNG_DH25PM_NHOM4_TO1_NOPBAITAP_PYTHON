'''
Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.

Trả lời:

1. Các loại lỗi khi lập trình:

-Lỗi cú pháp (Syntax Error)
Xảy ra khi mã nguồn vi phạm quy tắc cú pháp của ngôn ngữ lập trình.
Python không thể hiểu hoặc dịch đoạn mã đó.
Ví dụ: thiếu dấu hai chấm :, thiếu dấu ngoặc, sai indent…

-Lỗi ngoại lệ (Exception/Error)
Xảy ra trong quá trình chạy chương trình khi gặp tình huống không thể xử lý được.
Ví dụ: chia cho 0, truy cập chỉ số ngoài phạm vi mảng, lỗi kiểu dữ liệu...

-Lỗi logic (Logic Error)
Chương trình chạy không lỗi cú pháp hay ngoại lệ, nhưng kết quả trả về không đúng như mong đợi.
Khó phát hiện vì chương trình vẫn chạy bình thường.
Ví dụ: tính sai công thức, sai điều kiện if, sai thuật toán...

2. Cách bắt lỗi trong Python:

Python cung cấp cơ chế bắt ngoại lệ bằng các từ khóa: try, except, else, finally. Cách này giúp chương trình không bị dừng đột ngột khi gặp lỗi, mà xử lý hoặc thông báo lỗi một cách có kiểm soát.
'''