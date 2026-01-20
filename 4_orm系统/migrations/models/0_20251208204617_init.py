from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clas` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL COMMENT '班级名称'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL COMMENT '姓名',
    `pwd` VARCHAR(30) NOT NULL COMMENT '密码',
    `age` INT NOT NULL COMMENT '年龄',
    `sex` VARCHAR(10) NOT NULL COMMENT '性别',
    `sno` INT NOT NULL COMMENT '学号',
    `clas_id` INT NOT NULL,
    CONSTRAINT `fk_student_clas_4be9b492` FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL COMMENT '姓名',
    `pwd` VARCHAR(30) NOT NULL COMMENT '密码',
    `age` INT NOT NULL COMMENT '年龄',
    `sex` VARCHAR(10) NOT NULL COMMENT '性别',
    `title` VARCHAR(30) NOT NULL COMMENT '职称'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(30) NOT NULL COMMENT '课程名称',
    `teacher_id` INT NOT NULL,
    CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_course` (
    `student_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cou_student_0d222b` (`student_id`, `course_id`)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztWVtvmzAU/isVT5uUTeTWpHtLs1XrurZS202T2goZMASF2CmYtVHFf59tTDAQKDRdQy"
    "tecjk+Nud8/nwu5lFZYBO6/uepC3zly96jgsAC0h8peWdPActlImUCAnSXKxqxhu4TDxiE"
    "yizg+pCKTOgbnrMkDkZUigLXZUJsUEUH2YkoQM5dADWCbUhm0KMD17dU7CATPkA//ruca5"
    "YDXTNlpmOyZ3O5RlZLLjtG5IgrsqfpmoHdYIES5eWKzDBaazuIMKkNEfQAgWx54gXMfGad"
    "8DL2KLI0UYlMlOaY0AKBSyR3K2JgYMTwo9ZE+2Czp3zqdQejwbi/PxhTFW7JWjIKI/cS36"
    "OJHIGzKyXk44CASIPDmODGv3PITWfA2wxdrJ8Bj5qcBS+Gqgy9WJDAl1CmFD/lJhj1oUk/"
    "IRjdBMOByn4fWKpSDdUFeNBciGwyo3/7agmEvycX0++Tiw999SNbG1NqR3w/EyM9PhSGjJ"
    "rWXAKZCXRgzO+BZ2qpkQR+nwQmZEbltuBQzDw6uYAu4G7nYReH8zJa5VV3oDKDw5hCsVQc"
    "Eg4Y7uEixPJDi94iKwEI2Nxq9mz2pDhc4cDz4cZAFo2Uh7JEpw1mbTB7hWA21i1IAxhQ9W"
    "YEs47ERgKBQQms1WJletLT7GxGrHoJgubyQA7JPIxH2IOOjU7giqN5TI0CyNjETRHFrpKV"
    "modiUcSnYg/cr+NdhiPUSeoaJNGZnVxOJ1+/KWFxEt0yfVTJwacAra4w+6y4LVsk4v8de0"
    "s2hRuvZfKk5IrHChBorjWi9BjhhT2O9hyuJCjFjq73QoxG88QgmXk4sGfyrCTtbuQClWvZ"
    "hBaWVgGxDxvKAMm94jrAl5TaQqBhcfZ9FgLDA7MflQDNSP7L+w0ULAZSqDcAR93Yp0XUWO"
    "02A0caoGocZaG947KJwQhHg5vgwBoPKsL4Igdbys3woQ79hPru6bev9ti1RK+nP4d+3Sr0"
    "6xbTr5ujn49wDfoJ7QbQT9+np3jYt0a7oR+706zX90gz2qYndS+8ZccTX0A3D7+q7Y5EjZ"
    "31OnLpvl2rk9yjvfVOJ/Ek2+ikOsN0p5PqZbKNTroN2r7T4RCWtzrxhcCGVke6KyhudaSr"
    "ibbVaVp07bStTtvqtK1O2+q0rc7TrQ5xiFsrIq4n7B7LsTowdv3q51nvsQvryjqvsZ9fUr"
    "7Tt9gT6DnGbFNNJ0ZKSzqQ6LQV3Ruq6P5CzxfnpGoIk6bsOIhVRzEVunrDYYXYRbUKgxcf"
    "yxQi9GjUAFGov00Au2q1RFqWSXOplD6RiPdfaRB/XJ6fFdx/JVMyQP5C1MFr0zFIZ891fH"
    "LbTFhLUGReM6MXvn/nyuB9OJ38yeI6/Xl+yFHAPrE9vgpf4LBein359BL+A14KZys="
)
