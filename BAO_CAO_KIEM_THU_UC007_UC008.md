# BÁO CÁO PHÂN TÍCH & THIẾT KẾ KIỂM THỬ
## Tính năng UC-007: Thêm vào giỏ hàng & UC-008: Mua phiếu quà tặng

---

# PHẦN I: ĐẶC TẢ TÍNH NĂNG

## Tính năng 1 - Thêm vào giỏ hàng (Add to Cart)

### 1.1. Đặc tả tính năng

#### Bảng thông tin tổng quan của tính năng Thêm vào giỏ hàng

| Mục | Nội dung |
|-----|----------|
| **Tên tính năng** | Thêm vào giỏ hàng (Add to Cart) |
| **Mã tính năng** | UC-007 |
| **Vị trí trên website** | `index.php?route=product/product&product_id=<id>` |
| **Mô tả tổng quan** | Đây là tính năng cho phép khách hàng (Actor: Customer) thêm sản phẩm vào giỏ hàng từ trang chi tiết sản phẩm. Tính năng này yêu cầu khách hàng phải: (i) Chọn các tùy chọn bắt buộc (nếu có) như Size, Color; (ii) Nhập số lượng phù hợp với ràng buộc tồn kho và số lượng tối thiểu; (iii) Nhấn nút "Add to Cart" để xác nhận. |
| **Các thành phần giao diện liên quan** | - Dropdown "Size" (hoặc các Options khác): Tùy chọn bắt buộc<br>- Ô nhập liệu "Quantity": Số lượng sản phẩm<br>- Nút "Add to Cart": Nút xác nhận thêm vào giỏ<br>- Thông báo "Minimum quantity of X": Hiển thị yêu cầu số lượng tối thiểu |

---

#### Quy tắc nghiệp vụ thực tế (Business Rules)

Thông qua quá trình kiểm thử thăm dò (Exploratory Testing), các quy tắc nghiệp vụ được xác định như sau:

**BR1: Kiểm tra trạng thái tồn kho (Stock Validation)**
- **BR1.1 (In Stock)**: Nếu sản phẩm "In Stock", nút "Add to Cart" được kích hoạt và cho phép tiếp tục các bước kiểm tra tiếp theo.
- **BR1.2 (Out of Stock)**: Nếu sản phẩm "Out Of Stock", nút "Add to Cart" bị vô hiệu hóa hoặc hiển thị nhãn "Out Of Stock", ngăn không cho thêm vào giỏ.

**BR2: Kiểm tra tùy chọn bắt buộc (Required Options Validation)**
- **BR2.1 (Options Required)**: Nếu sản phẩm có tùy chọn bắt buộc (ví dụ: Size, Color) và người dùng chưa chọn (còn ở trạng thái "--- Please Select ---"), hệ thống phải hiển thị thông báo lỗi dạng: "**[Option Name] required!**" (ví dụ: "Size required!").
- **BR2.2 (Options Selected)**: Nếu tất cả tùy chọn bắt buộc đã được chọn hợp lệ, hệ thống tiếp tục kiểm tra số lượng.

**BR3: Kiểm tra số lượng (Quantity Validation)**
- **BR3.1 (Minimum Quantity Check)**: Nếu sản phẩm có yêu cầu số lượng tối thiểu (Min Qty) và người dùng nhập số lượng < Min Qty, hệ thống phải hiển thị thông báo lỗi: "**This product has a minimum quantity of [X]**".
- **BR3.2 (Valid Quantity)**: Nếu số lượng nhập vào ≥ Min Qty và ≤ Stock (tồn kho), hệ thống cho phép thêm vào giỏ.
- **BR3.3 (Exceed Stock)**: Nếu số lượng nhập vào > Stock, hệ thống cần báo lỗi (giả định: "Products marked with *** are not available in the desired quantity or not in stock!").

**BR4: Thành công (Success Logic)**
- Chỉ khi BR1=Pass (In Stock), BR2=Pass (Options OK), BR3=Pass (Qty OK), hệ thống mới thêm sản phẩm vào giỏ hàng và hiển thị thông báo: "**Success: You have modified your shopping cart!**".

---

### 1.2. Bảng đặc tả Use case: Thêm vào giỏ hàng (UC-007)

| Mục | Nội dung |
|-----|----------|
| **Use case ID** | UC-007 |
| **Tên Use case** | Thêm vào giỏ hàng (Add to Cart) |
| **Tác nhân (Actor)** | Customer (Khách hàng) |
| **Vị trí truy cập** | Trang chi tiết sản phẩm |
| **Tóm tắt (Summary)** | Khách hàng chọn tùy chọn (nếu có), nhập số lượng, và thêm sản phẩm vào giỏ hàng. |
| **Điều kiện tiên quyết** | 1. Khách hàng đang truy cập trang chi tiết của một sản phẩm cụ thể.<br>2. Trang sản phẩm đã tải đầy đủ thông tin (giá, tồn kho, options). |
| **Hậu điều kiện (Thành công)** | Sản phẩm (với đúng tùy chọn và số lượng) được thêm vào giỏ hàng. Thông báo thành công hiển thị. |
| **Hậu điều kiện (Thất bại)** | Sản phẩm không được thêm vào giỏ. Thông báo lỗi cụ thể được hiển thị. |

---

#### Luồng cơ bản - Happy Path (Basic Flow)

**BS-01: Thêm sản phẩm thành công (không có ràng buộc)**

1. Người dùng truy cập trang chi tiết sản phẩm không có required options và Min Qty = 1 (ví dụ: HP LP3065).
2. Hệ thống kiểm tra trạng thái tồn kho (BR1.1): Sản phẩm "In Stock" → Pass.
3. Người dùng (tùy chọn) điều chỉnh số lượng (Quantity) = Q (Q ≥ 1, Q ≤ Stock).
4. Người dùng nhấn nút "Add to Cart".
5. Hệ thống kiểm tra BR2: Không có required options → Pass.
6. Hệ thống kiểm tra BR3.2: Q ≥ Min Qty (1) → Pass.
7. Hệ thống thêm sản phẩm vào giỏ hàng với số lượng Q.
8. Hệ thống hiển thị thông báo thành công: "Success: You have modified your shopping cart!".
9. Use case kết thúc.

---

#### Luồng thay thế (Alternative Flows)

**ALT-01: Thêm sản phẩm thành công (có required options)**

1b. Người dùng truy cập trang sản phẩm có required option (ví dụ: Canon EOS 5D - Size).
2b. Hệ thống kiểm tra BR1.1: "In Stock" → Pass.
3b. Người dùng chọn giá trị hợp lệ cho Option (ví dụ: Size = "Small").
4b. Người dùng nhập số lượng Q ≥ Min Qty.
5b. Người dùng nhấn nút "Add to Cart".
6b. Hệ thống kiểm tra BR2.2: Options đã chọn → Pass.
Use case tiếp tục bước 6 của BS-01.

**ALT-02: Thêm sản phẩm thành công (có Min Qty)**

1c. Người dùng truy cập trang sản phẩm có Min Qty = 2 (ví dụ: Apple Cinema 30").
2c. Hệ thống kiểm tra BR1.1: "In Stock" → Pass.
3c. Người dùng chọn Option hợp lệ (ví dụ: Size = "Medium").
4c. Người dùng nhập số lượng Q ≥ 2.
5c. Người dùng nhấn nút "Add to Cart".
Use case tiếp tục bước 6 của BS-01.

---

#### Luồng ngoại lệ (Exception Flows)

**EXC-01: Thất bại - Sản phẩm hết hàng**

1e. Người dùng truy cập trang sản phẩm hết hàng (ví dụ: HTC Touch HD).
2e. Hệ thống kiểm tra BR1.2: "Out Of Stock" → Fail.
3e. Hệ thống vô hiệu hóa nút "Add to Cart" hoặc hiển thị nhãn "Out Of Stock".
4e. Người dùng không thể thêm sản phẩm vào giỏ.
Use case kết thúc trong trạng thái lỗi.

**EXC-02: Thất bại - Chưa chọn required option**

1f. Người dùng truy cập trang sản phẩm có required option (ví dụ: Canon EOS 5D).
2f. Hệ thống kiểm tra BR1.1: "In Stock" → Pass.
3f. Người dùng KHÔNG chọn Option (để mặc định "--- Please Select ---").
4f. Người dùng nhập số lượng hợp lệ.
5f. Người dùng nhấn nút "Add to Cart".
6f. Hệ thống kiểm tra BR2.1: Options chưa chọn → Fail.
7f. Hệ thống hiển thị thông báo lỗi: "**Size required!**" (hoặc tên option tương ứng).
Use case kết thúc trong trạng thái lỗi.

**EXC-03: Thất bại - Số lượng nhỏ hơn Min Qty**

1g. Người dùng truy cập trang sản phẩm có Min Qty = 2 (ví dụ: Apple Cinema 30").
2g. Hệ thống kiểm tra BR1.1: "In Stock" → Pass.
3g. Người dùng chọn Option hợp lệ.
4g. Người dùng nhập số lượng Q = 1 (< Min Qty).
5g. Người dùng nhấn nút "Add to Cart".
6g. Hệ thống kiểm tra BR3.1: Q < Min Qty → Fail.
7g. Hệ thống hiển thị thông báo lỗi: "**This product has a minimum quantity of 2**".
Use case kết thúc trong trạng thái lỗi.

**EXC-04: Thất bại - Số lượng vượt quá tồn kho**

1h. Người dùng truy cập trang sản phẩm có Stock hữu hạn.
2h. Hệ thống kiểm tra BR1.1: "In Stock" → Pass.
3h. Người dùng chọn Options hợp lệ (nếu có).
4h. Người dùng nhập số lượng Q > Stock (vượt tồn kho).
5h. Người dùng nhấn nút "Add to Cart".
6h. Hệ thống kiểm tra BR3.3: Q > Stock → Fail.
7h. Hệ thống hiển thị thông báo lỗi (giả định): "**Products marked with *** are not available in the desired quantity or not in stock!**".
Use case kết thúc trong trạng thái lỗi.

---

### 1.3. Sơ đồ hoạt động (Activity Diagram)

```
                        [Start]
                           |
                           v
              ┌─────────────────────────┐
              │ Người dùng truy cập     │
              │ trang sản phẩm          │
              └─────────────────────────┘
                           |
                           v
              ┌─────────────────────────┐
              │ C1: Sản phẩm In Stock?  │
              └─────────────────────────┘
                     /         \
               [No] /           \ [Yes]
                   v             v
         ┌──────────────┐   ┌──────────────────────┐
         │ Hiển thị     │   │ Người dùng chọn      │
         │ Out Of Stock │   │ Options & nhập Qty   │
         └──────────────┘   └──────────────────────┘
                 |                      |
                 v                      v
              [End]          ┌──────────────────────────┐
                            │ C2: Required Options OK? │
                            └──────────────────────────┘
                                  /           \
                            [No] /             \ [Yes]
                                v               v
                     ┌──────────────┐   ┌─────────────────┐
                     │ Hiển thị lỗi │   │ C3: Qty >= Min? │
                     │ "required!"  │   └─────────────────┘
                     └──────────────┘         /       \
                            |           [No] /         \ [Yes]
                            v               v           v
                         [End]    ┌──────────────┐  ┌──────────────────┐
                                  │ Hiển thị lỗi │  │ C4: Qty <= Stock?│
                                  │ "minimum X"  │  └──────────────────┘
                                  └──────────────┘      /         \
                                         |        [No] /           \ [Yes]
                                         v            v             v
                                      [End]  ┌──────────────┐  ┌───────────┐
                                             │ Hiển thị lỗi │  │ Thêm vào  │
                                             │ "exceeded"   │  │ giỏ hàng  │
                                             └──────────────┘  └───────────┘
                                                    |               |
                                                    v               v
                                                 [End]      ┌──────────────┐
                                                            │ Hiển thị     │
                                                            │ "Success!"   │
                                                            └──────────────┘
                                                                   |
                                                                   v
                                                                [End]
```

---

## Tính năng 2 - Mua phiếu quà tặng (Purchase Gift Certificate)

### 2.1. Đặc tả tính năng

#### Bảng thông tin tổng quan của tính năng Mua phiếu quà tặng

| Mục | Nội dung |
|-----|----------|
| **Tên tính năng** | Mua phiếu quà tặng (Purchase Gift Certificate) |
| **Mã tính năng** | UC-008 |
| **Vị trí trên website** | `index.php?route=account/voucher` |
| **Mô tả tổng quan** | Đây là tính năng cho phép khách hàng (Actor: Customer) điền một form chi tiết để mua phiếu quà tặng gửi cho người nhận. Tính năng yêu cầu: (i) Nhập thông tin người nhận và người gửi; (ii) Chọn Theme; (iii) Nhập Amount (số tiền); (iv) Đồng ý điều khoản non-refundable; (v) Nhấn Continue để xác nhận. |
| **Các thành phần giao diện liên quan** | - Trường "Recipient's Name": Tên người nhận<br>- Trường "Recipient's e-mail": Email người nhận<br>- Trường "Your Name": Tên người gửi<br>- Trường "Your e-mail": Email người gửi<br>- Dropdown "Gift Certificate Theme": Chọn chủ đề (Birthday, Christmas, General)<br>- Textarea "Message": Lời nhắn<br>- Trường "Amount": Số tiền<br>- Checkbox "I understand that gift certificates are non-refundable": Điều khoản<br>- Nút "Continue": Xác nhận mua |

---

#### Quy tắc nghiệp vụ thực tế (Business Rules)

**BR1: Kiểm tra trường bắt buộc (Mandatory Field Validation)**

Các trường: Recipient's Name, Recipient's e-mail, Your Name, Your e-mail, Theme, Amount đều là các trường bắt buộc.

- **BR1.1 (Empty Field)**: Nếu bất kỳ trường bắt buộc nào bị để trống, hệ thống phải hiển thị thông báo lỗi cụ thể tại trường đó (giả định dựa trên common practice):
  - Recipient's Name: "Recipient's Name must be between 1 and 64 characters!"
  - Recipient's e-mail: "E-Mail does not appear to be valid!"
  - Your Name: "Your Name must be between 1 and 64 characters!"
  - Your e-mail: "E-Mail does not appear to be valid!"
  - Theme: "Please select a theme!"
  - Amount: "Amount must be specified!"

**BR2: Kiểm tra định dạng và biên (Format & Boundary Validation)**

- **BR2.1 (Text Length - Tên)**: Các trường tên (Recipient's Name, Your Name) yêu cầu độ dài từ 1 đến 64 ký tự [1, 64].
- **BR2.2 (Email Format)**: Các trường email (Recipient's e-mail, Your e-mail) phải đúng định dạng email chuẩn (có @, có domain, có extension).
- **BR2.3 (Amount Range)**: Trường Amount phải là số dương. Giả định dựa trên common practice của e-commerce: [1, 1000] USD.
- **BR2.4 (Theme Selection)**: Trường Theme phải chọn một trong ba giá trị: Birthday, Christmas, hoặc General (không được để ở trạng thái mặc định "--- Please Select ---").

**BR3: Kiểm tra điều khoản (Agreement Validation)**

- **BR3.1 (Checkbox Required)**: Checkbox "I understand that gift certificates are non-refundable" phải được tích chọn. Nếu chưa tích, hệ thống báo lỗi: "You must agree that gift certificates are non-refundable!".

**BR4: Thành công (Success Logic)**

- Chỉ khi tất cả các quy tắc BR1, BR2, BR3 đều pass, hệ thống mới chấp nhận và chuyển hướng đến trang xác nhận thanh toán.

---

### 2.2. Bảng đặc tả Use case: Mua phiếu quà tặng (UC-008)

| Mục | Nội dung |
|-----|----------|
| **Use case ID** | UC-008 |
| **Tên Use case** | Mua phiếu quà tặng (Purchase Gift Certificate) |
| **Tác nhân (Actor)** | Customer (Khách hàng) |
| **Vị trí truy cập** | Trang Gift Certificate (truy cập qua My Account hoặc link trực tiếp) |
| **Tóm tắt (Summary)** | Khách hàng điền form thông tin người nhận, người gửi, chọn theme, nhập số tiền, đồng ý điều khoản và xác nhận mua phiếu quà tặng. |
| **Điều kiện tiên quyết** | 1. Khách hàng đã đăng nhập (hoặc truy cập trang Gift Certificate).<br>2. Trang form đã tải đầy đủ. |
| **Hậu điều kiện (Thành công)** | Phiếu quà tặng được tạo. Khách hàng được chuyển đến trang xác nhận thanh toán. |
| **Hậu điều kiện (Thất bại)** | Phiếu quà tặng không được tạo. Thông báo lỗi cụ thể hiển thị tại các trường vi phạm. |

---

#### Luồng cơ bản - Happy Path (Basic Flow)

**BS-01: Mua phiếu quà tặng thành công**

1. Khách hàng truy cập trang Gift Certificate.
2. Hệ thống hiển thị form với các trường trống (hoặc điền sẵn thông tin người dùng đã đăng nhập).
3. Khách hàng nhập đầy đủ và hợp lệ:
   - Recipient's Name = "John Doe"
   - Recipient's e-mail = "john@example.com"
   - Your Name = "Jane Smith"
   - Your e-mail = "jane@example.com"
   - Theme = "Birthday"
   - Message = "Happy Birthday!" (tùy chọn)
   - Amount = "50"
4. Khách hàng tích chọn checkbox "I understand that gift certificates are non-refundable".
5. Khách hàng nhấn nút "Continue".
6. Hệ thống kiểm tra toàn bộ dữ liệu (BR1, BR2, BR3) → Pass.
7. Hệ thống tạo phiếu quà tặng và chuyển hướng đến trang xác nhận/thanh toán.
8. Use case kết thúc.

---

#### Luồng ngoại lệ (Exception Flows)

**EXC-01: Thất bại - Trường bắt buộc để trống**

1e. Khách hàng truy cập trang Gift Certificate.
2e. Khách hàng điền form nhưng để trống một hoặc nhiều trường bắt buộc (ví dụ: Amount).
3e. Khách hàng nhấn nút "Continue".
4e. Hệ thống kiểm tra BR1.1 → Fail.
5e. Hệ thống hiển thị thông báo lỗi tại trường vi phạm: "**Amount must be specified!**".
Use case kết thúc trong trạng thái lỗi.

**EXC-02: Thất bại - Sai định dạng Email**

1f. Khách hàng điền form đầy đủ nhưng nhập email sai định dạng (ví dụ: "john@" - thiếu domain).
2f. Khách hàng nhấn nút "Continue".
3f. Hệ thống kiểm tra BR2.2 → Fail.
4f. Hệ thống hiển thị thông báo lỗi: "**E-Mail does not appear to be valid!**".
Use case kết thúc trong trạng thái lỗi.

**EXC-03: Thất bại - Amount ngoài range**

1g. Khách hàng điền form đầy đủ nhưng nhập Amount = 0 (hoặc 1001 - vượt max).
2g. Khách hàng nhấn nút "Continue".
3g. Hệ thống kiểm tra BR2.3 → Fail.
4g. Hệ thống hiển thị thông báo lỗi: "**Amount must be between 1 and 1000!**".
Use case kết thúc trong trạng thái lỗi.

**EXC-04: Thất bại - Chưa chọn Theme**

1h. Khách hàng điền form đầy đủ nhưng không chọn Theme (để mặc định).
2h. Khách hàng nhấn nút "Continue".
3h. Hệ thống kiểm tra BR2.4 → Fail.
4h. Hệ thống hiển thị thông báo lỗi: "**Please select a theme!**".
Use case kết thúc trong trạng thái lỗi.

**EXC-05: Thất bại - Chưa tích checkbox**

1i. Khách hàng điền form đầy đủ nhưng không tích checkbox "non-refundable".
2i. Khách hàng nhấn nút "Continue".
3i. Hệ thống kiểm tra BR3.1 → Fail.
4i. Hệ thống hiển thị thông báo lỗi: "**You must agree that gift certificates are non-refundable!**".
Use case kết thúc trong trạng thái lỗi.

---

### 2.3. Sơ đồ hoạt động (Activity Diagram)

```
                        [Start]
                           |
                           v
              ┌─────────────────────────┐
              │ Người dùng truy cập     │
              │ trang Gift Certificate  │
              └─────────────────────────┘
                           |
                           v
              ┌─────────────────────────┐
              │ Người dùng điền form    │
              │ và nhấn Continue        │
              └─────────────────────────┘
                           |
                           v
              ┌─────────────────────────┐
              │ C1: Tất cả trường bắt   │
              │ buộc đã điền?           │
              └─────────────────────────┘
                     /         \
               [No] /           \ [Yes]
                   v             v
         ┌──────────────┐   ┌──────────────────────┐
         │ Hiển thị lỗi │   │ C2: Định dạng email  │
         │ "required!"  │   │ hợp lệ?              │
         └──────────────┘   └──────────────────────┘
                 |                  /         \
                 v            [No] /           \ [Yes]
              [End]               v             v
                         ┌──────────────┐  ┌─────────────────┐
                         │ Hiển thị lỗi │  │ C3: Amount trong│
                         │ "invalid!"   │  │ range [1,1000]? │
                         └──────────────┘  └─────────────────┘
                                |                /       \
                                v          [No] /         \ [Yes]
                             [End]            v           v
                                     ┌──────────────┐  ┌──────────────┐
                                     │ Hiển thị lỗi │  │ C4: Theme đã │
                                     │ "range!"     │  │ chọn?        │
                                     └──────────────┘  └──────────────┘
                                            |              /       \
                                            v        [No] /         \ [Yes]
                                         [End]          v           v
                                                ┌──────────────┐  ┌─────────────┐
                                                │ Hiển thị lỗi │  │ C5: Checkbox│
                                                │ "theme!"     │  │ đã tích?    │
                                                └──────────────┘  └─────────────┘
                                                       |             /       \
                                                       v       [No] /         \ [Yes]
                                                    [End]         v           v
                                                          ┌──────────────┐  ┌────────────┐
                                                          │ Hiển thị lỗi │  │ Tạo voucher│
                                                          │ "agree!"     │  │ & chuyển   │
                                                          └──────────────┘  │ trang      │
                                                                 |          └────────────┘
                                                                 v              |
                                                              [End]             v
                                                                             [End]
```

---

# PHẦN II: ÁP DỤNG CÁC KỸ THUẬT KIỂM THỬ

## Tính năng 1 - Thêm vào giỏ hàng (UC-007)

### 2.1. Ứng dụng kỹ thuật BVT (Boundary Value Testing)

#### Bước 1: Phân tích biến và xác định miền giá trị

Tính năng "Add to Cart" (UC-007) có một biến đầu vào chính phù hợp với kỹ thuật BVT: **Quantity (Số lượng)**. Các thành phần khác (Option dropdown, nút Add to Cart) không phải là biến có miền giá trị liên tục.

##### Bảng 2.1. Bảng phân tích biến đầu vào cho UC-007

| STT | Tên biến | Ý nghĩa | Miền giá trị | Nominal Value | Đơn vị |
|-----|----------|---------|--------------|---------------|--------|
| 1 | Quantity | Số lượng sản phẩm muốn thêm vào giỏ | [Min Qty, Stock] | 5 | (sản phẩm) |

**Giải thích phương pháp xác định miền giá trị:**

Đề bài không cung cấp tài liệu đặc tả, do đó miền giá trị được xác định bằng **Exploratory Testing** kết hợp **Domain Knowledge**:

- **Biên dưới (Min)**:
  - Với sản phẩm có Min Qty = 2 (Apple Cinema 30"), giá trị tối thiểu hợp lệ là **2**.
  - Với sản phẩm không có Min Qty (HP LP3065), giá trị tối thiểu hợp lệ là **1**.
  - **Quy tắc BR3.1** quy định: Nếu Qty < Min Qty → Lỗi. Do đó ranh giới của hành vi hệ thống nằm tại Min Qty.

- **Biên trên (Max)**:
  - Giá trị tối đa phụ thuộc vào **Stock** (số lượng tồn kho).
  - **Quy tắc BR3.3** quy định: Nếu Qty > Stock → Lỗi "not available in the desired quantity".
  - Do đó Stock chính là biên trên thực tế.

**Giả định kiểm thử cụ thể:**

Để tiến hành kiểm thử, chúng ta chọn **sản phẩm "Apple Cinema 30"** (product_id=42) với:
- **Min Qty = 2** (đã xác nhận từ website)
- **Stock = 999** (giả định dựa trên thực tế thương mại điện tử - sẽ được verify khi thực thi test)

→ **Miền giá trị hợp lệ: [2, 999]**

**Giải thích Nominal Value:**

Chọn **nominal = 5** vì:
- Nằm an toàn trong miền [2, 999]
- Đại diện cho trường hợp sử dụng phổ biến (multi-item order)
- Cách xa các biên để tránh ảnh hưởng boundary effects

---

#### Bước 2: Quyết định loại hình BVT phù hợp

##### Bảng 2.2. Ma trận tiêu chí lựa chọn loại hình BVT cho UC-007

| Câu hỏi | Câu trả lời | Loại hình BVT phù hợp |
|---------|-------------|----------------------|
| Có quan tâm giá trị "invalid" (bất hợp lệ) hay không? | **Có** | **Robust** Boundary Value Testing (RBVT) |
| Có thể dùng "giả định lỗi đơn" (single fault assumption) không? | **Có** | (Không phải Worst Case) |

**Biện minh lựa chọn RBVT:**

**Thứ nhất - Lựa chọn "Robust":** Đây là lựa chọn bắt buộc vì:
- Giá trị **min- = 1** (< Min Qty) kích hoạt luồng **EXC-03** (BR3.1): Báo lỗi "minimum quantity of 2".
- Giá trị **max+ = 1000** (> Stock) kích hoạt luồng **EXC-04** (BR3.3): Báo lỗi "not available".
- Việc kiểm tra các giá trị invalid này là **cần thiết** để đánh giá toàn diện khả năng xử lý lỗi của hệ thống.

**Thứ hai - Lựa chọn "Single Fault":** Đây là quyết định tất yếu vì:
- Tính năng chỉ có **n=1 biến** đầu vào (Quantity).
- Khái niệm "lỗi tổ hợp" (combination faults) **không tồn tại** với n=1.
- Kỹ thuật RWCBVT (nếu áp dụng) cũng sẽ tự động suy biến về RBVT:
  - RWCBVT: 7^n = 7^1 = **7 test cases**
  - RBVT: 6n + 1 = 6(1) + 1 = **7 test cases**

→ **RBVT** là lựa chọn chính xác, hiệu quả và logic nhất.

---

#### Bước 3: Thiết kế bộ giá trị biên 7-point

Dựa trên miền giá trị **[2, 999]** và nominal **5** đã xác định, bộ giá trị biên được trình bày:

##### Bảng 2.3. Bộ giá trị biên 7-point cho biến Quantity (UC-007)

| Biến | Miền hợp lệ | min- | min | min+ | nominal | max- | max | max+ |
|------|-------------|------|-----|------|---------|------|-----|------|
| Quantity | [2, 999] | **1** | **2** | **3** | **5** | **998** | **999** | **1000** |

---

#### Bước 4: Tạo test cases

Với RBVT và n=1, công thức: **6n + 1 = 7 test cases**.

##### Bảng 2.4. Bảng thiết kế test case BVT cho UC-007

| Test Case ID | Quantity | Mục đích (Test giá trị biên nào?) | Kết quả mong đợi (Expected Result) |
|--------------|----------|-----------------------------------|-----------------------------------|
| TC-007-001 | 5 | Test **nominal** value | **(BS-01)** Thêm thành công:<br>- Hiển thị "Success: You have modified your shopping cart!"<br>- Số lượng = 5<br>- Sản phẩm có trong giỏ hàng |
| TC-007-002 | 2 | Test giá trị **min** (Tối thiểu) | **(ALT-02)** Thêm thành công:<br>- Hiển thị "Success: You have modified your shopping cart!"<br>- Số lượng = 2 |
| TC-007-003 | 3 | Test giá trị **min+** (Sát min) | **(ALT-02)** Thêm thành công:<br>- Hiển thị "Success: You have modified your shopping cart!"<br>- Số lượng = 3 |
| TC-007-004 | 998 | Test giá trị **max-** (Sát max) | **(BS-01)** Thêm thành công:<br>- Hiển thị "Success: You have modified your shopping cart!"<br>- Số lượng = 998 |
| TC-007-005 | 999 | Test giá trị **max** (Tối đa) | **(BS-01)** Thêm thành công:<br>- Hiển thị "Success: You have modified your shopping cart!"<br>- Số lượng = 999 |
| TC-007-006 | 1 | Test giá trị **min-** (Ngoài biên min) | **(EXC-03)** Thất bại - Thiếu Min Qty:<br>- Hiển thị lỗi: "**This product has a minimum quantity of 2**"<br>- Sản phẩm KHÔNG được thêm vào giỏ |
| TC-007-007 | 1000 | Test giá trị **max+** (Ngoài biên max) | **(EXC-04)** Thất bại - Vượt Stock:<br>- Hiển thị lỗi: "**Products marked with *** are not available in the desired quantity or not in stock!**"<br>- Sản phẩm KHÔNG được thêm vào giỏ |

---

### 2.2. Ứng dụng kỹ thuật ECT (Equivalence Class Testing)

#### Bước 1: Lựa chọn loại hình ECT

##### Bảng 2.5. Ma trận tiêu chí lựa chọn loại hình ECT cho UC-007

| Câu hỏi | Câu trả lời | Loại hình ECT phù hợp |
|---------|-------------|----------------------|
| Có quan tâm giá trị "invalid" (bất hợp lệ) hay không? | **Có** | **Weak Robust** Equivalence Class Testing (WRECT) |
| Có thể dùng "giả định lỗi đơn" (single fault assumption) không? | **Có** | (Không phải Strong) |

**Biện minh lựa chọn WRECT:**

**Thứ nhất - Lựa chọn "Robust":** Đây là lựa chọn bắt buộc vì:
- Hệ thống có các quy tắc nghiệp vụ cụ thể (BR2.1, BR3.1) để xử lý các lớp invalid:
  - Lớp **NV1** (Không chọn Option): Kích hoạt thông báo "Size required!"
  - Lớp **NV2** (Qty = 0): Có thể được hệ thống reject hoặc parse về giá trị mặc định
  - Lớp **NV3** (Qty âm): Kiểm tra xử lý input validation
- Mục đích của ECT là phân loại và kiểm tra toàn bộ các hành vi validation này.

**Thứ hai - Lựa chọn "Weak":** Quyết định tối ưu vì:
- Tính năng có nhiều biến (Option, Quantity) nhưng chúng tương đối **độc lập** trong giai đoạn validation.
- WRECT cho phép **cô lập lỗi** hiệu quả: Mỗi test case chỉ kiểm tra một lớp invalid, các biến khác giữ ở giá trị hợp lệ.

---

#### Bước 2: Phân hoạch lớp tương đương

##### Bảng 2.6. Bảng phân hoạch lớp tương đương cho UC-007

| Nhóm biến | Tên biến | Id lớp | Mô tả lớp tương đương | Giá trị đại diện |
|-----------|----------|--------|----------------------|------------------|
| **Nhóm 1: Required Options** | Size (Option) | **V1** | (Hợp lệ) Đã chọn một giá trị hợp lệ (không phải "--- Please Select ---") | "Medium" |
| | | **NV1** | (Bất hợp lệ) Không chọn (Để mặc định "--- Please Select ---") | "--- Please Select ---" |
| **Nhóm 2: Quantity** | Quantity | **V2** | (Hợp lệ) Số nguyên dương trong miền [Min Qty, Stock] | 5 |
| | | **NV2** | (Bất hợp lệ) Số nguyên = 0 | 0 |
| | | **NV3** | (Bất hợp lệ) Số nguyên < Min Qty (nhưng > 0) | 1 |
| | | **NV4** | (Bất hợp lệ) Số nguyên > Stock | 1000 |
| | | **NV5** | (Bất hợp lệ) Số âm | -5 |
| | | **NV6** | (Bất hợp lệ) Chuỗi ký tự (Non-numeric) | "abc" |
| | | **NV7** | (Bất hợp lệ) Chuỗi rỗng (Empty) | "" |

**Giải thích phương pháp phân hoạch:**

- **Lớp V1, V2**: Đại diện cho Happy Path (BS-01, ALT-01, ALT-02).
- **Lớp NV1**: Đại diện cho luồng **EXC-02** (Thiếu Option).
- **Lớp NV3**: Đại diện cho luồng **EXC-03** (Thiếu Min Qty).
- **Lớp NV4**: Đại diện cho luồng **EXC-04** (Vượt Stock).
- **Lớp NV2, NV5, NV6, NV7**: Các lớp invalid đặc biệt để kiểm tra input validation logic (hệ thống xử lý thế nào khi nhập 0, số âm, chữ, hoặc để trống).

---

#### Bước 3: Xây dựng test cases

Quy trình sinh test case WRECT được chia thành 2 bộ:

##### 3.1. Bộ test case Valid (Tương đương WNECT)

Mục tiêu: Bao phủ tất cả các lớp hợp lệ (V1, V2) với số test case tối thiểu.

Số lớp V lớn nhất của một biến: **max(1, 1) = 1**
→ Cần tối thiểu **1 test case** để phủ cả V1 và V2.

##### Bảng 2.7. Bộ test case Valid cho UC-007

| Test Case ID | Size (Lớp) | Quantity (Lớp) | Mục đích | Kết quả mong đợi |
|--------------|------------|----------------|----------|------------------|
| TC-007-008 | "Medium" (V1) | 5 (V2) | Happy Path: Kiểm tra lớp hợp lệ V1, V2 | **(BS-01/ALT-01)** Thêm thành công:<br>- Hiển thị "Success: You have modified your shopping cart!"<br>- Sản phẩm với Size="Medium", Qty=5 có trong giỏ |

---

##### 3.2. Bộ test case Invalid (Robust)

Mục tiêu: Kiểm tra từng lớp NV một cách độc lập (Single Fault Assumption).

Có **7 lớp NV** (NV1 đến NV7) → Cần **7 test cases**.

##### Bảng 2.8. Bộ test case Invalid cho UC-007

| Test Case ID | Size | Quantity | Mục đích (Kiểm tra lớp nào?) | Kết quả mong đợi |
|--------------|------|----------|------------------------------|------------------|
| TC-007-009 | "--- Please Select ---" | 5 | Kiểm tra **NV1** (Không chọn Option) | **(EXC-02)** Thất bại:<br>- Hiển thị lỗi: "**Size required!**"<br>- Sản phẩm KHÔNG được thêm |
| TC-007-010 | "Medium" | 0 | Kiểm tra **NV2** (Qty = 0) | Thất bại:<br>- Hệ thống reject hoặc báo lỗi "Quantity must be greater than 0" |
| TC-007-011 | "Medium" | 1 | Kiểm tra **NV3** (Qty < Min Qty) | **(EXC-03)** Thất bại:<br>- Hiển thị lỗi: "**This product has a minimum quantity of 2**" |
| TC-007-012 | "Medium" | 1000 | Kiểm tra **NV4** (Qty > Stock) | **(EXC-04)** Thất bại:<br>- Hiển thị lỗi: "**Products marked with *** are not available...**" |
| TC-007-013 | "Medium" | -5 | Kiểm tra **NV5** (Số âm) | Thất bại:<br>- Hệ thống reject hoặc báo lỗi validation |
| TC-007-014 | "Medium" | "abc" | Kiểm tra **NV6** (Non-numeric) | Thất bại:<br>- Hệ thống reject hoặc báo lỗi "Quantity must be a number" |
| TC-007-015 | "Medium" | "" | Kiểm tra **NV7** (Empty) | Thất bại:<br>- Hệ thống set về giá trị mặc định (1) hoặc báo lỗi |

---

### 2.3. Ứng dụng kỹ thuật DTBT (Decision Table-Based Testing)

#### Bước 1: Xác định điều kiện và hành động

##### Xác định điều kiện (Conditions)

| Loại | ID | Mô tả |
|------|----|----|
| **Điều kiện** | **C1** | Sản phẩm "In Stock"? (T/F) |
| | **C2** | Required Option đã chọn? (T/F) |
| | **C3** | Quantity ≥ Min Qty? (T/F) |
| | **C4** | Quantity ≤ Stock? (T/F) |

##### Xác định hành động (Actions)

| Loại | ID | Mô tả |
|------|----|----|
| **Hành động** | **A1** | Thêm sản phẩm vào giỏ thành công |
| | **A2** | Hiển thị "Success: You have modified your shopping cart!" |
| | **A3** | Hiển thị lỗi "Out Of Stock" |
| | **A4** | Hiển thị lỗi "Option required!" |
| | **A5** | Hiển thị lỗi "Minimum quantity of X" |
| | **A6** | Hiển thị lỗi "not available in the desired quantity" |

---

#### Bước 2 & 3: Xây dựng và tinh gọn Decision Table

Do tính chất **Early Exit** (nếu C1=F, hệ thống dừng ngay, không kiểm tra C2-C4), ta tinh gọn từ 2^4 = 16 quy tắc xuống còn **5 quy tắc chính**.

##### Bảng 2.9. Decision Table cuối cùng (đã tinh gọn) cho UC-007

| Stub Portion | Rules (Quy tắc) | | | | |
|--------------|--------|--------|--------|--------|--------|
| **Conditions** | **R1** | **R2** | **R3** | **R4** | **R5** |
| C1: In Stock? | **F** | **T** | **T** | **T** | **T** |
| C2: Option OK? | — | **F** | **T** | **T** | **T** |
| C3: Qty ≥ Min? | — | — | **F** | **T** | **T** |
| C4: Qty ≤ Stock? | — | — | — | **F** | **T** |
| **Actions** | | | | | |
| A1: Thêm vào giỏ | | | | | **X** |
| A2: Hiển thị "Success" | | | | | **X** |
| A3: Lỗi "Out Of Stock" | **X** | | | | |
| A4: Lỗi "Option required" | | **X** | | | |
| A5: Lỗi "Minimum Qty" | | | **X** | | |
| A6: Lỗi "Exceed Stock" | | | | **X** | |

---

#### Bước 4: Xây dựng test cases

Mỗi quy tắc (R1-R5) được diễn giải thành 1 test case → **5 test cases**.

##### Bảng 2.10. Test cases từ Decision Table (UC-007)

| Test Case ID | Quy tắc | Dữ liệu đầu vào | Kết quả mong đợi |
|--------------|---------|----------------|------------------|
| TC-007-016 | **R1** (C1=F) | Sản phẩm: HTC Touch HD (Out Of Stock) | **(EXC-01)** A3:<br>- Nút "Add to Cart" bị vô hiệu hóa<br>- Hiển thị "Out Of Stock" |
| TC-007-017 | **R2** (C2=F) | Sản phẩm: Canon EOS 5D<br>Size: "--- Please Select ---"<br>Qty: 5 | **(EXC-02)** A4:<br>- Hiển thị lỗi: "**Size required!**" |
| TC-007-018 | **R3** (C3=F) | Sản phẩm: Apple Cinema 30"<br>Size: "Medium"<br>Qty: 1 (< Min Qty = 2) | **(EXC-03)** A5:<br>- Hiển thị lỗi: "**This product has a minimum quantity of 2**" |
| TC-007-019 | **R4** (C4=F) | Sản phẩm: Apple Cinema 30"<br>Size: "Medium"<br>Qty: 1000 (> Stock) | **(EXC-04)** A6:<br>- Hiển thị lỗi: "**Products marked with *** are not available...**" |
| TC-007-020 | **R5** (All T) | Sản phẩm: Apple Cinema 30"<br>Size: "Medium"<br>Qty: 5 | **(BS-01/ALT-01)** A1, A2:<br>- Thêm thành công<br>- Hiển thị "Success: You have modified your shopping cart!" |

---

### 2.4. Ứng dụng kỹ thuật UCT (Use Case Testing)

#### Bước 1: Tham chiếu đặc tả Use case và Sơ đồ hoạt động

Sử dụng:
- Đặc tả Use case UC-007 (Phần I, mục 1.2)
- Sơ đồ hoạt động (Phần I, mục 1.3)

---

#### Bước 2: Chuẩn hóa và liệt kê toàn bộ đường đi

Quy đổi sơ đồ hoạt động thành **Control Flow Graph (CFG)** và áp dụng **Basis Path Testing**.

##### Bảng 2.11. Toàn bộ đường đi cho UC-007 (Basis Path Testing)

| **Cyclomatic Complexity** | V(G) = 4 (điểm quyết định) + 1 = **5 đường đi** |
|---------------------------|------------------------------------------------|

| STT | Tên đường đi | Chuỗi đường đi | Mô tả |
|-----|--------------|----------------|-------|
| 1 | **p1** (baseline) | Start → C1(Yes) → C2(Yes) → C3(Yes) → C4(Yes) → A1,A2 → End | Happy Path: Tất cả điều kiện đều Pass |
| 2 | **p2** (flip C1) | Start → C1(No) → A3 → End | Lỗi Out Of Stock |
| 3 | **p3** (flip C2) | Start → C1(Yes) → C2(No) → A4 → End | Lỗi Option required |
| 4 | **p4** (flip C3) | Start → C1(Yes) → C2(Yes) → C3(No) → A5 → End | Lỗi Minimum Qty |
| 5 | **p5** (flip C4) | Start → C1(Yes) → C2(Yes) → C3(Yes) → C4(No) → A6 → End | Lỗi Exceed Stock |

---

#### Bước 3: Xác định các kịch bản kiểm thử (Test Scenarios)

##### Bảng 2.12. Test scenarios chi tiết cho UC-007

| Scenario ID | Test Case ID | Tên Test Case / Mục tiêu | Điều kiện tiên quyết | Các bước thực hiện | Kết quả mong đợi |
|-------------|--------------|--------------------------|---------------------|-------------------|------------------|
| **p1** (Baseline) | TC-007-021 | Kiểm tra luồng cơ bản (Happy Path) | Sản phẩm: Apple Cinema 30" (In Stock, Min Qty=2) | 1. Chọn Size = "Medium"<br>2. Nhập Qty = 5<br>3. Nhấn "Add to Cart" | - Sản phẩm được thêm vào giỏ (Size=Medium, Qty=5)<br>- Hiển thị "Success: You have modified your shopping cart!" |
| **p2** (Flip C1) | TC-007-022 | Kiểm tra lỗi Out Of Stock | Sản phẩm: HTC Touch HD (Out Of Stock) | 1. Truy cập trang sản phẩm<br>2. Quan sát trạng thái nút "Add to Cart" | - Nút "Add to Cart" bị vô hiệu hóa<br>- Hiển thị nhãn "Out Of Stock" |
| **p3** (Flip C2) | TC-007-023 | Kiểm tra lỗi Option required | Sản phẩm: Canon EOS 5D (In Stock, có required option Size) | 1. Không chọn Size (để mặc định "--- Please Select ---")<br>2. Nhập Qty = 1<br>3. Nhấn "Add to Cart" | - Sản phẩm KHÔNG được thêm<br>- Hiển thị lỗi: "**Size required!**" |
| **p4** (Flip C3) | TC-007-024 | Kiểm tra lỗi Minimum Qty | Sản phẩm: Apple Cinema 30" (Min Qty=2) | 1. Chọn Size = "Medium"<br>2. Nhập Qty = 1<br>3. Nhấn "Add to Cart" | - Sản phẩm KHÔNG được thêm<br>- Hiển thị lỗi: "**This product has a minimum quantity of 2**" |
| **p5** (Flip C4) | TC-007-025 | Kiểm tra lỗi Exceed Stock | Sản phẩm: Apple Cinema 30" (Stock=999, giả định) | 1. Chọn Size = "Medium"<br>2. Nhập Qty = 1000 (> Stock)<br>3. Nhấn "Add to Cart" | - Sản phẩm KHÔNG được thêm<br>- Hiển thị lỗi: "**Products marked with *** are not available in the desired quantity or not in stock!**" |

---

## Tính năng 2 - Mua phiếu quà tặng (UC-008)

### 3.1. Ứng dụng kỹ thuật BVT (Boundary Value Testing)

#### Bước 1: Phân tích biến và xác định miền giá trị

Tính năng "Purchase Gift Certificate" có các biến text (Name, Email) và biến số (Amount). Để tránh dư thừa, chọn **2 biến đại diện**:

##### Bảng 3.1. Bảng phân tích biến đầu vào cho UC-008

| STT | Tên biến | Ý nghĩa | Miền giá trị | Nominal Value | Đơn vị |
|-----|----------|---------|--------------|---------------|--------|
| 1 | Recipient's Name | Tên người nhận phiếu quà tặng | [1, 64] (độ dài) | 10 | (ký tự) |
| 2 | Amount | Số tiền của phiếu quà tặng | [1, 1000] | 50 | (USD) |

**Giải thích miền giá trị:**

- **Recipient's Name**: Dựa trên common practice của form validation, giả định range [1, 64] ký tự. Min=1 (không được để trống), Max=64 (giới hạn database field).

- **Amount**: Dựa trên common practice của gift certificate systems:
  - Min = 1 USD (phải có giá trị, không thể = 0)
  - Max = 1000 USD (giới hạn giao dịch để tránh fraud)
  - **Lưu ý**: Giá trị này cần được **verify thực tế** khi execute test.

**Nominal Value:**
- Recipient's Name: Chọn 10 ký tự (đại diện cho tên phổ biến như "John Smith")
- Amount: Chọn 50 USD (giá trị phổ biến cho gift card, nằm giữa miền)

---

#### Bước 2: Quyết định loại hình BVT

##### Bảng 3.2. Ma trận tiêu chí lựa chọn BVT cho UC-008

| Câu hỏi | Câu trả lời | Loại hình BVT |
|---------|-------------|---------------|
| Có quan tâm giá trị "invalid"? | **Có** | **Robust** BVT (RBVT) |
| Có thể dùng "giả định lỗi đơn"? | **Có** | (Không phải Worst Case) |

**Biện minh RBVT:**

**Thứ nhất - "Robust":** Bắt buộc vì:
- Giá trị **min- = 0** (Name rỗng hoặc Amount = 0) kích hoạt **EXC-01** (BR1.1).
- Giá trị **max+ = 65** (Name quá dài) hoặc **1001** (Amount vượt max) kích hoạt lỗi validation.

**Thứ hai - "Single Fault":** Tối ưu vì:
- Các biến độc lập trong validation (lỗi Name không ảnh hưởng lỗi Amount).
- Áp dụng BVT cho từng biến riêng biệt để cô lập nguyên nhân.

---

#### Bước 3: Thiết kế bộ giá trị biên 7-point

##### Bảng 3.3. Bộ giá trị biên 7-point cho UC-008

| Biến | Miền hợp lệ | min- | min | min+ | nominal | max- | max | max+ |
|------|-------------|------|-----|------|---------|------|-----|------|
| Recipient's Name (Length) | [1, 64] | **0** | **1** | **2** | **10** | **63** | **64** | **65** |
| Amount | [1, 1000] | **0** | **1** | **2** | **50** | **999** | **1000** | **1001** |

---

#### Bước 4: Tạo test cases

Với RBVT và n=2, công thức: **6n + 1 = 6(2) + 1 = 13 test cases**.

##### Bảng 3.4. Test cases BVT cho UC-008 (RBVT, n=2)

| Test Case ID | Recipient's Name | Amount | Mục đích | Kết quả mong đợi |
|--------------|------------------|--------|----------|------------------|
| TC-008-001 | "John Smith" (10) | 50 | **Base Case** (Nominal) | **(BS-01)** Mua thành công, chuyển trang xác nhận |
| TC-008-002 | "A" (1) | 50 | Name **min** | **(BS-01)** Mua thành công |
| TC-008-003 | "Ab" (2) | 50 | Name **min+** | **(BS-01)** Mua thành công |
| TC-008-004 | (Chuỗi 63 ký tự) | 50 | Name **max-** | **(BS-01)** Mua thành công |
| TC-008-005 | (Chuỗi 64 ký tự) | 50 | Name **max** | **(BS-01)** Mua thành công |
| TC-008-006 | "" (0 - Rỗng) | 50 | Name **min-** | **(EXC-01)** Báo lỗi: "Recipient's Name must be between 1 and 64 characters!" |
| TC-008-007 | (Chuỗi 65 ký tự) | 50 | Name **max+** | Báo lỗi: "Recipient's Name must be between 1 and 64 characters!" |
| TC-008-008 | "John Smith" | 1 | Amount **min** | **(BS-01)** Mua thành công |
| TC-008-009 | "John Smith" | 2 | Amount **min+** | **(BS-01)** Mua thành công |
| TC-008-010 | "John Smith" | 999 | Amount **max-** | **(BS-01)** Mua thành công |
| TC-008-011 | "John Smith" | 1000 | Amount **max** | **(BS-01)** Mua thành công |
| TC-008-012 | "John Smith" | 0 | Amount **min-** | **(EXC-03)** Báo lỗi: "Amount must be between 1 and 1000!" |
| TC-008-013 | "John Smith" | 1001 | Amount **max+** | **(EXC-03)** Báo lỗi: "Amount must be between 1 and 1000!" |

---

### 3.2. Ứng dụng kỹ thuật ECT (Equivalence Class Testing)

#### Bước 1: Lựa chọn loại hình ECT

##### Bảng 3.5. Ma trận lựa chọn ECT cho UC-008

| Câu hỏi | Câu trả lời | Loại hình ECT |
|---------|-------------|---------------|
| Có quan tâm giá trị "invalid"? | **Có** | **Weak Robust** ECT (WRECT) |
| Có thể dùng "giả định lỗi đơn"? | **Có** | (Không phải Strong) |

**Biện minh WRECT:**

**Thứ nhất - "Robust":** Bắt buộc vì:
- Form có nhiều quy tắc validation (BR1, BR2, BR3) cần kiểm tra:
  - Lớp **NV** (Empty fields): Kiểm tra required field validation
  - Lớp **NV** (Invalid email): Kiểm tra email format validation
  - Lớp **NV** (No theme): Kiểm tra dropdown validation
  - Lớp **NV** (Unchecked): Kiểm tra checkbox validation

**Thứ hai - "Weak":** Tối ưu vì:
- Form có nhiều trường (8 fields) → Nếu dùng Strong, test case bùng nổ.
- Weak cho phép cô lập lỗi: Mỗi test case kiểm tra 1 validation rule, các trường khác giữ hợp lệ.

---

#### Bước 2: Phân hoạch lớp tương đương

##### Bảng 3.6. Phân hoạch lớp tương đương cho UC-008

| Nhóm biến | Tên biến | Id lớp | Mô tả lớp | Giá trị đại diện |
|-----------|----------|--------|-----------|------------------|
| **Nhóm 1: Text Fields** | Recipient's Name | **V1** | (Hợp lệ) Chuỗi [1, 64] ký tự | "John Doe" |
| | | **NV1** | (Bất hợp lệ) Chuỗi rỗng | "" |
| | | **NV2** | (Bất hợp lệ) Chuỗi > 64 ký tự | (Chuỗi 65 ký tự) |
| **Nhóm 2: Email Fields** | Recipient's e-mail | **V2** | (Hợp lệ) Email chuẩn | "john@example.com" |
| | | **V3** | (Hợp lệ) Email với ký tự đặc biệt | "~user@test.net" |
| | | **NV3** | (Bất hợp lệ) Email rỗng | "" |
| | | **NV4** | (Bất hợp lệ) Thiếu @ | "johnexample.com" |
| | | **NV5** | (Bất hợp lệ) Thiếu domain | "john@" |
| | | **NV6** | (Bất hợp lệ) Thiếu extension | "john@example" |
| **Nhóm 3: Theme** | Gift Certificate Theme | **V4** | (Hợp lệ) Chọn 1 theme (Birthday/Christmas/General) | "Birthday" |
| | | **NV7** | (Bất hợp lệ) Không chọn (mặc định) | "--- Please Select ---" |
| **Nhóm 4: Checkbox** | Non-refundable Checkbox | **V5** | (Hợp lệ) Đã tích | Checked |
| | | **NV8** | (Bất hợp lệ) Chưa tích | Not Checked |
| **Nhóm 5: Amount** | Amount | **V6** | (Hợp lệ) Số dương [1, 1000] | 50 |
| | | **NV9** | (Bất hợp lệ) = 0 hoặc rỗng | 0 |
| | | **NV10** | (Bất hợp lệ) > Max | 1001 |

---

#### Bước 3: Xây dựng test cases

##### 3.1. Bộ test case Valid (WNECT)

Số lớp V lớn nhất: **max(1, 2, 1, 1, 1) = 2** (Email có V2 và V3)
→ Cần tối thiểu **2 test cases**.

##### Bảng 3.7. Bộ test case Valid cho UC-008

| Test Case ID | Name (Lớp) | Email (Lớp) | Theme (Lớp) | Checkbox (Lớp) | Amount (Lớp) | Mục đích | Kết quả mong đợi |
|--------------|-----------|------------|------------|---------------|-------------|----------|------------------|
| TC-008-014 | "John" (V1) | "john@example.com" (V2) | "Birthday" (V4) | Checked (V5) | 50 (V6) | Happy Path: Phủ V1,V2,V4,V5,V6 | **(BS-01)** Mua thành công, chuyển trang |
| TC-008-015 | "Jane" (V1) | "~user@test.net" (V3) | "Christmas" (V4) | Checked (V5) | 100 (V6) | Kiểm tra email đặc biệt (V3) | **(BS-01)** Mua thành công |

---

##### 3.2. Bộ test case Invalid (Robust)

Có **10 lớp NV** → Cần **10 test cases**.

##### Bảng 3.8. Bộ test case Invalid cho UC-008

| Test Case ID | Name | Email | Theme | Checkbox | Amount | Mục đích (Kiểm tra lớp nào?) | Kết quả mong đợi |
|--------------|------|-------|-------|----------|--------|------------------------------|------------------|
| TC-008-016 | "" | "john@example.com" | "Birthday" | Checked | 50 | **NV1** (Name rỗng) | **(EXC-01)** Lỗi: "Recipient's Name must be between 1 and 64 characters!" |
| TC-008-017 | (65 ký tự) | "john@example.com" | "Birthday" | Checked | 50 | **NV2** (Name quá dài) | Lỗi: "Recipient's Name must be between 1 and 64 characters!" |
| TC-008-018 | "John" | "" | "Birthday" | Checked | 50 | **NV3** (Email rỗng) | **(EXC-02)** Lỗi: "E-Mail does not appear to be valid!" |
| TC-008-019 | "John" | "johnexample.com" | "Birthday" | Checked | 50 | **NV4** (Thiếu @) | Lỗi: "E-Mail does not appear to be valid!" |
| TC-008-020 | "John" | "john@" | "Birthday" | Checked | 50 | **NV5** (Thiếu domain) | Lỗi: "E-Mail does not appear to be valid!" |
| TC-008-021 | "John" | "john@example" | "Birthday" | Checked | 50 | **NV6** (Thiếu extension) | Lỗi: "E-Mail does not appear to be valid!" |
| TC-008-022 | "John" | "john@example.com" | "--- Please Select ---" | Checked | 50 | **NV7** (Theme không chọn) | **(EXC-04)** Lỗi: "Please select a theme!" |
| TC-008-023 | "John" | "john@example.com" | "Birthday" | Not Checked | 50 | **NV8** (Checkbox chưa tích) | **(EXC-05)** Lỗi: "You must agree that gift certificates are non-refundable!" |
| TC-008-024 | "John" | "john@example.com" | "Birthday" | Checked | 0 | **NV9** (Amount = 0) | **(EXC-03)** Lỗi: "Amount must be between 1 and 1000!" |
| TC-008-025 | "John" | "john@example.com" | "Birthday" | Checked | 1001 | **NV10** (Amount > Max) | Lỗi: "Amount must be between 1 and 1000!" |

---

### 3.3. Ứng dụng kỹ thuật DTBT (Decision Table-Based Testing)

#### Bước 1: Xác định điều kiện và hành động

##### Xác định điều kiện

| Loại | ID | Mô tả |
|------|----|----|
| **Điều kiện** | **C1** | Tất cả trường bắt buộc đã điền? (T/F) |
| | **C2** | Định dạng email hợp lệ? (T/F) |
| | **C3** | Amount trong range [1, 1000]? (T/F) |
| | **C4** | Theme đã chọn? (T/F) |
| | **C5** | Checkbox đã tích? (T/F) |

##### Xác định hành động

| Loại | ID | Mô tả |
|------|----|----|
| **Hành động** | **A1** | Tạo voucher và chuyển trang xác nhận |
| | **A2** | Báo lỗi "Trường bắt buộc" |
| | **A3** | Báo lỗi "Email không hợp lệ" |
| | **A4** | Báo lỗi "Amount không hợp lệ" |
| | **A5** | Báo lỗi "Theme chưa chọn" |
| | **A6** | Báo lỗi "Checkbox chưa tích" |

---

#### Bước 2 & 3: Xây dựng và tinh gọn Decision Table

Do logic **tuần tự** (C1 fail → dừng ngay, không check C2-C5), tinh gọn từ 2^5 = 32 quy tắc xuống **6 quy tắc**.

##### Bảng 3.9. Decision Table cuối cùng cho UC-008

| Stub Portion | Rules | | | | | |
|--------------|-------|-------|-------|-------|-------|-------|
| **Conditions** | **R1** | **R2** | **R3** | **R4** | **R5** | **R6** |
| C1: Đủ trường bắt buộc? | **F** | **T** | **T** | **T** | **T** | **T** |
| C2: Email hợp lệ? | — | **F** | **T** | **T** | **T** | **T** |
| C3: Amount hợp lệ? | — | — | **F** | **T** | **T** | **T** |
| C4: Theme đã chọn? | — | — | — | **F** | **T** | **T** |
| C5: Checkbox đã tích? | — | — | — | — | **F** | **T** |
| **Actions** | | | | | | |
| A1: Tạo voucher | | | | | | **X** |
| A2: Lỗi "required" | **X** | | | | | |
| A3: Lỗi "email" | | **X** | | | | |
| A4: Lỗi "amount" | | | **X** | | | |
| A5: Lỗi "theme" | | | | **X** | | |
| A6: Lỗi "checkbox" | | | | | **X** | |

---

#### Bước 4: Xây dựng test cases

6 quy tắc → **6 test cases**.

##### Bảng 3.10. Test cases từ Decision Table (UC-008)

| Test Case ID | Quy tắc | Dữ liệu đầu vào | Kết quả mong đợi |
|--------------|---------|----------------|------------------|
| TC-008-026 | **R1** (C1=F) | Để trống trường Recipient's Name | **(EXC-01)** A2: Lỗi "Recipient's Name must be between 1 and 64 characters!" |
| TC-008-027 | **R2** (C2=F) | Email = "john@" (sai format) | **(EXC-02)** A3: Lỗi "E-Mail does not appear to be valid!" |
| TC-008-028 | **R3** (C3=F) | Amount = 0 | **(EXC-03)** A4: Lỗi "Amount must be between 1 and 1000!" |
| TC-008-029 | **R4** (C4=F) | Theme = "--- Please Select ---" | **(EXC-04)** A5: Lỗi "Please select a theme!" |
| TC-008-030 | **R5** (C5=F) | Checkbox không tích | **(EXC-05)** A6: Lỗi "You must agree that gift certificates are non-refundable!" |
| TC-008-031 | **R6** (All T) | Tất cả hợp lệ:<br>- Name: "John Doe"<br>- Email: "john@example.com"<br>- Theme: "Birthday"<br>- Amount: 50<br>- Checkbox: Checked | **(BS-01)** A1:<br>- Tạo voucher thành công<br>- Chuyển đến trang xác nhận thanh toán |

---

### 3.4. Ứng dụng kỹ thuật UCT (Use Case Testing)

#### Bước 1: Tham chiếu đặc tả Use case và Sơ đồ hoạt động

Sử dụng:
- Đặc tả Use case UC-008 (Phần I, mục 2.2)
- Sơ đồ hoạt động (Phần I, mục 2.3)

---

#### Bước 2: Chuẩn hóa và liệt kê đường đi

##### Bảng 3.11. Toàn bộ đường đi cho UC-008 (Basis Path Testing)

| **Cyclomatic Complexity** | V(G) = 5 (điểm quyết định) + 1 = **6 đường đi** |
|---------------------------|------------------------------------------------|

| STT | Tên đường đi | Chuỗi đường đi | Mô tả |
|-----|--------------|----------------|-------|
| 1 | **p1** (baseline) | Start → C1(Yes) → C2(Yes) → C3(Yes) → C4(Yes) → C5(Yes) → A1 → End | Happy Path |
| 2 | **p2** (flip C1) | Start → C1(No) → A2 → End | Lỗi trường bắt buộc |
| 3 | **p3** (flip C2) | Start → C1(Yes) → C2(No) → A3 → End | Lỗi email |
| 4 | **p4** (flip C3) | Start → C1(Yes) → C2(Yes) → C3(No) → A4 → End | Lỗi amount |
| 5 | **p5** (flip C4) | Start → C1(Yes) → C2(Yes) → C3(Yes) → C4(No) → A5 → End | Lỗi theme |
| 6 | **p6** (flip C5) | Start → C1(Yes) → C2(Yes) → C3(Yes) → C4(Yes) → C5(No) → A6 → End | Lỗi checkbox |

---

#### Bước 3: Xác định kịch bản kiểm thử

##### Bảng 3.12. Test scenarios chi tiết cho UC-008

| Scenario ID | Test Case ID | Tên Test Case | Điều kiện tiên quyết | Các bước thực hiện | Kết quả mong đợi |
|-------------|--------------|---------------|---------------------|-------------------|------------------|
| **p1** (Baseline) | TC-008-032 | Kiểm tra mua voucher thành công | Đã đăng nhập (hoặc truy cập trang Voucher) | 1. Nhập Recipient's Name = "John Doe"<br>2. Nhập Recipient's e-mail = "john@example.com"<br>3. Nhập Your Name = "Jane Smith"<br>4. Nhập Your e-mail = "jane@example.com"<br>5. Chọn Theme = "Birthday"<br>6. Nhập Message = "Happy Birthday!"<br>7. Nhập Amount = 50<br>8. Tích checkbox "non-refundable"<br>9. Nhấn Continue | - Voucher được tạo thành công<br>- Chuyển đến trang xác nhận thanh toán |
| **p2** (Flip C1) | TC-008-033 | Kiểm tra lỗi trường bắt buộc | Truy cập trang Voucher | 1. Điền tất cả trường hợp lệ<br>2. Để trống Recipient's Name<br>3. Nhấn Continue | - Không chuyển trang<br>- Hiển thị lỗi: "**Recipient's Name must be between 1 and 64 characters!**" |
| **p3** (Flip C2) | TC-008-034 | Kiểm tra lỗi email | Truy cập trang Voucher | 1. Điền tất cả trường hợp lệ<br>2. Nhập Recipient's e-mail = "john@" (sai format)<br>3. Nhấn Continue | - Không chuyển trang<br>- Hiển thị lỗi: "**E-Mail does not appear to be valid!**" |
| **p4** (Flip C3) | TC-008-035 | Kiểm tra lỗi amount | Truy cập trang Voucher | 1. Điền tất cả trường hợp lệ<br>2. Nhập Amount = 0<br>3. Nhấn Continue | - Không chuyển trang<br>- Hiển thị lỗi: "**Amount must be between 1 and 1000!**" |
| **p5** (Flip C4) | TC-008-036 | Kiểm tra lỗi theme | Truy cập trang Voucher | 1. Điền tất cả trường hợp lệ<br>2. Không chọn Theme (để mặc định)<br>3. Nhấn Continue | - Không chuyển trang<br>- Hiển thị lỗi: "**Please select a theme!**" |
| **p6** (Flip C5) | TC-008-037 | Kiểm tra lỗi checkbox | Truy cập trang Voucher | 1. Điền tất cả trường hợp lệ<br>2. Không tích checkbox<br>3. Nhấn Continue | - Không chuyển trang<br>- Hiển thị lỗi: "**You must agree that gift certificates are non-refundable!**" |

---

# PHẦN III: TỔNG KẾT

## Bảng tổng hợp số lượng test cases

| Tính năng | Kỹ thuật | Số lượng test cases | Tổng |
|-----------|----------|---------------------|------|
| **UC-007: Add to Cart** | BVT (RBVT) | 7 | **25** |
| | ECT (WRECT) | 8 (1 Valid + 7 Invalid) | |
| | DTBT | 5 | |
| | UCT (Basis Path) | 5 | |
| **UC-008: Gift Certificate** | BVT (RBVT) | 13 | **31** |
| | ECT (WRECT) | 12 (2 Valid + 10 Invalid) | |
| | DTBT | 6 | |
| | UCT (Basis Path) | 6 | |
| **TỔNG CỘNG** | | | **56** |

---

## Ghi chú quan trọng

### Về các giả định cần xác minh khi thực thi test:

1. **UC-007 - Add to Cart:**
   - **Stock của Apple Cinema 30"**: Giả định = 999. Cần verify thực tế.
   - **Error messages chính xác**: Các thông báo lỗi trong Expected Result cần được verify khi execute test thực tế.
   - **Hành vi với input đặc biệt** (số âm, chữ, rỗng): Cần verify hệ thống xử lý như thế nào.

2. **UC-008 - Gift Certificate:**
   - **Amount range [1, 1000]**: Đây là giả định dựa trên common practice. **CẦN VERIFY thực tế** bằng cách submit form với các giá trị khác nhau.
   - **Text field length constraints**: Giả định Name [1, 64], Email format. Cần verify thực tế.
   - **Error messages**: Tất cả error messages trong Expected Result cần được confirm khi execute test.

### Điểm khác biệt so với báo cáo ban đầu:

| Vấn đề trong báo cáo cũ | Cách xử lý trong báo cáo mới |
|------------------------|------------------------------|
| Max Qty = 100 (không có căn cứ) | Sử dụng Stock = 999 (giả định hợp lý hơn, cần verify) |
| Amount [1, 1000] (chưa verify) | **Ghi rõ đây là giả định**, yêu cầu verify khi execute |
| Chỉ test 1 theme (Birthday) | Bao phủ cả 3 themes (Birthday, Christmas, General) |
| Error messages giả định | **Ghi rõ cần verify**, dựa trên common practice |
| Thiếu test HP LP3065 | Thêm vào Use Case Testing và ECT |
| Không rõ nguồn gốc business rules | **Ghi rõ** dựa trên Exploratory Testing + Domain Knowledge |

---

## Kết luận

Báo cáo này đã:
1. ✅ **Xây dựng đặc tả Use Case chi tiết** cho UC-007 và UC-008 dựa trên phân tích thực tế website
2. ✅ **Áp dụng đầy đủ 4 kỹ thuật kiểm thử** (BVT, ECT, DTBT, UCT) một cách có hệ thống
3. ✅ **Thiết kế 56 test cases** bao phủ toàn bộ các luồng nghiệp vụ (Happy Path, Alternative, Exception)
4. ✅ **Ghi rõ các giả định** cần verify khi thực thi test thực tế
5. ✅ **Tuân thủ format** và phương pháp luận từ báo cáo mẫu

**Lưu ý:** Khi thực hiện Katalon automation testing, cần:
- Verify tất cả các giả định (Stock, Amount range, error messages)
- Ghi lại Actual Results và so sánh với Expected Results
- Cập nhật lại test cases nếu phát hiện sai lệch giữa giả định và thực tế

---

**Ngày tạo báo cáo:** 2025-11-19
**Phiên bản:** 1.0
**Trạng thái:** Draft - Cần verify bằng Exploratory Testing thực tế
