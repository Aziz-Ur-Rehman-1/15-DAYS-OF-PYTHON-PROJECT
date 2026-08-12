import qrcode
import os

def generate_qr():
    text_or_url = input("\nEnter Website URL or Text to convert into QR Code: ").strip()
    if not text_or_url:
        print("\nInput cannot be empty!\n")
        return

    filename = input("Enter output filename (default: my_qrcode.png): ").strip()
    if not filename:
        filename = "my_qrcode.png"
    if not filename.endswith(".png"):
        filename += ".png"

    try:
        # Configure QR Code settings
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text_or_url)
        qr.make(fit=True)

        # Create image and save
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)

        full_path = os.path.abspath(filename)
        print("\n" + "="*50)
        print(f" SUCCESS! QR Code generated successfully.")
        print(f" Saved at: {full_path}")
        print("="*50 + "\n")

    except Exception as e:
        print(f"\nError generating QR Code: {e}\n")

def main():
    while True:
        print("Select an Option:")
        print("1. Generate New QR Code")
        print("2. Exit")

        choice = input("\nEnter choice (1-2): ").strip()

        if choice == "1":
            generate_qr()
        elif choice == "2":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()