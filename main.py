from app import create_app

if __name__ == "__main__":
    # For local development (not for production)
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)

