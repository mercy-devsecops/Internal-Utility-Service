from app import app


def check_app():
    print("Starting CI checks...")

    # test if Flask app exists
    if app:
        print("✔ App loaded successfully")
    else:
        print("❌ App failed to load")
        return False

    # simple sanity message check
    response = app.test_client().get("/")
    
    if response.status_code == 200:
        print("✔ Homepage is working")
    else:
        print("❌ Homepage failed")
        return False

    print("✔ CI CHECK PASSED")
    return True


if __name__ == "__main__":
    if not check_app():
        exit(1)
