#Which of the following are equivalent to O(N)? 
#1/đúng vì:Khi P < N/2, thì P thực sự là một hằng số và không thể lớn hơn N/2. Khi chúng ta thêm một hằng số vào độ phức tạp thời gian, nó không thay đổi tỷ lệ tăng của độ phức tạp theo quy mô dữ liệu đầu vào. Do đó, chúng ta có thể xấp xỉ O(N + P) thành O(N).
#2/đúng vì:hằng số nhân không ảnh hưởng đến độ phức tạp theo cách nào cả. Do đó, O(2N) có thể xấp xỉ thành O(N) trong phân tích độ phức tạp.
#3/đúng vì:nếu chúng ta có một hàm có độ phức tạp là O(N + log N), thì trong trường hợp lớn, thành phần O(log N) không ảnh hưởng lớn đến độ tăng tổng thể của hàm theo N. Do đó, nó có thể xấp xỉ là O(N).
#4/sai vì:biểu thức O(N + N log N) thực sự là O(N log N) và không phải là O(N). Điều này bởi vì khi kích thước dữ liệu N tăng lớn, thành phần N log N sẽ chiếm ưu thế và quyết định độ tăng tổng thể của hàm.
#5/sai vì:khi có biểu thức O(N + M), chúng ta nên giữ nguyên và không thể xấp xỉ nó thành O(N) mà không xác định rõ mối quan hệ giữa N và M.