-- Sample data for local development / demos.
-- Run after schema.sql and seed.sql.

WITH demo_user AS (
    SELECT id FROM users WHERE email = 'demo@interviewiq.dev'
)
INSERT INTO interview_history (user_id, role_title, question, answer, feedback, score, mode)
SELECT id, 'Backend Engineer',
       'Tell me about a time you optimized a slow database query.',
       'I profiled the query, added a composite index, and cut latency by 80%.',
       'Good structure, consider quantifying impact on user-facing metrics too.',
       82, 'text'
FROM demo_user;

WITH demo_user AS (
    SELECT id FROM users WHERE email = 'demo@interviewiq.dev'
)
INSERT INTO progress (user_id, questions_asked, grammar_score, vocabulary_score, interview_score, resume_score, weekly_progress)
SELECT id, 12, 78, 65, 82, 70, 40
FROM demo_user
ON CONFLICT (user_id) DO NOTHING;
