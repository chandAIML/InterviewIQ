-- Baseline seed data for a fresh InterviewIQ install.
-- Password for the demo user below is "Password123!" (bcrypt hash placeholder;
-- regenerate with the app's hash_password() before using in a real environment).

INSERT INTO users (id, full_name, email, hashed_password, is_active, is_admin)
VALUES (
    uuid_generate_v4(),
    'Demo User',
    'demo@interviewiq.dev',
    '$2b$12$replace-with-a-real-bcrypt-hash-------------------',
    TRUE,
    FALSE
)
ON CONFLICT (email) DO NOTHING;
