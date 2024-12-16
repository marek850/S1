--CREATE UNIQUE INDEX idx_comments_comment_id ON comments(comment_id);*

CREATE INDEX idx_comments_post_id ON comments(post_id); *

--CREATE UNIQUE INDEX idx_users_user_id ON users(user_id);*

--CREATE INDEX idx_comments_user_id ON comments(user_id);

--CREATE INDEX idx_likes_post_user ON likes(post_id, user_id); *

CREATE INDEX idx_posts_created_at ON posts(created_at DESC); *

CREATE INDEX idx_posts_user_id ON posts(user_id); *

CREATE INDEX idx_users_email ON users(email);  * 

--CREATE INDEX idx_posts_user_id_created ON posts(user_id, created_at DESC);
CREATE INDEX idx_likes_post_id ON likes(post_id); *




DROP INDEX idx_posts_user_id_created;



CREATE INDEX idx_posts_created_at_user_id ON posts(created_at DESC, post_id);
CREATE INDEX idx_users_user_id ON users(user_id);
CREATE INDEX idx_likes_post_id_user ON likes(post_id, user_id);

--drops
DROP INDEX idx_users_user_id;
DROP INDEX idx_comments_comment_id;
DROP INDEX idx_likes_post_id;