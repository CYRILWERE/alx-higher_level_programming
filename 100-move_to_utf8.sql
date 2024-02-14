/*
 * Task: Convert hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
 * Convert the following to UTF8:
 * - Database hbtn_0c_0
 * - Table first_table
 * - Field name in first_table
 */

/* Convert database to utf8mb4 */
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

/* Convert table to utf8mb4 */
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

/* Convert field to utf8mb4 */
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

