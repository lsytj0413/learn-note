-- init database

DROP DATABASE IF EXISTS awesome;

CREATE DATABASE awesome;
USE awesome;


GRANT SELECT, INSERT, UPDATE, DELETE ON awesome.* TO 'www-data'@'localhost' IDENTIFIED BY 'www-data';


-- 用户表
CREATE TABLE users (
       `id` VARCHAR(50) NOT NULL,
       `email` VARCHAR(50) NOT NULL,
       `password` VARCHAR(50) NOT NULL,
       `admin` BOOL NOT NULL,
       `name` VARCHAR(50) NOT NULL,
       `image` VARCHAR(500) NOT NULL,
       `created_at` REAL NOT NULL,
       UNIQUE KEY `idx_email` (`email`),
       KEY `idx_created_at` (`created_at`),
       PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- 博客文章表
CREATE TABLE blogs (
       `id` VARCHAR(50) NOT NULL,
       `user_id` VARCHAR(50) NOT NULL,
       `user_name` VARCHAR(50) NOT NULL,
       `user_image` VARCHAR(500) NOT NULL,
       `name` VARCHAR(50) NOT NULL,
       `summary` VARCHAR(200) NOT NULL,
       `content` MEDIUMTEXT NOT NULL,
       `created_at` REAL NOT NULL,
       KEY `idx_created_at` (`created_at`),
       PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- 文章评论表
CREATE TABLE comments(
       `id` VARCHAR(50) NOT NULL,
       `blog_id` VARCHAR(50) NOT NULL,
       `user_id` VARCHAR(50) NOT NULL,
       `user_name` VARCHAR(50) NOT NULL,
       `user_image` VARCHAR(500) NOT NULL,
       `content` MEDIUMTEXT NOT NULL,
       `created_at` REAL NOT NULL,
       KEY `idx_created_at` (`created_at`),
       PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- 创建一个用户
INSERT INTO users (`id`, `email`, `password`, `admin`, `name`, `created_at`, `image`)
VALUES (
       '0010018336417540987fff4508f43fbaed718e263442526000',
       'admin@example.com',
       '5f4dcc3b5aa765d61d8327deb882cf99',
       1,
       'Administrator',
       1402909113.628,
       ''
);


INSERT INTO blogs (`id`, `user_id`, `user_name`, `user_image`, `name`, `summary`, `content`, `created_at`)
VALUES (
       '0010018336417540987fff4508f43fbaed718e263442526000',
       '0010018336417540987fff4508f43fbaed718e263442526000',
       'Administrator',
       '',
       'testBlog',
       'testBlogSummary',
       'testBlogContent',
       1402909113.628
);
