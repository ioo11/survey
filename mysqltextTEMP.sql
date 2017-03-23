CREATE TABLE `Test` (
	`id` int NOT NULL,
	`name` varchar(30) NOT NULL,
	`pub_date` DATE NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Question` (
	`id` int NOT NULL AUTO_INCREMENT,
	`id_test` int NOT NULL,
	`type` ENUM('E', 'S', 'T') NOT NULL,
	`text` varchar(250) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Enum_answer` (
	`id` int NOT NULL,
	`id_question` int NOT NULL,
	`text` varchar(100) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Set_answer` (
	`id` int NOT NULL,
	`id_question` int NOT NULL,
	`text` varchar(100) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Selected_enum_answer` (
	`id` int NOT NULL,
	`id_session` int NOT NULL,
	`id_selected_enum` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Selected_set_answer` (
	`id` int NOT NULL,
	`id_session` int NOT NULL,
	`id_selected_set` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Selected_text_answer` (
	`id` int NOT NULL,
	`id_session` int NOT NULL,
	`id_question` int NOT NULL,
	`answer` TEXT(250) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Session` (
	`id` int NOT NULL,
	`id_test` int NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Question` ADD CONSTRAINT `Question_fk0` FOREIGN KEY (`id_test`) REFERENCES `Test`(`id`);

ALTER TABLE `Enum_answer` ADD CONSTRAINT `Enum_answer_fk0` FOREIGN KEY (`id_question`) REFERENCES `Question`(`id`);

ALTER TABLE `Set_answer` ADD CONSTRAINT `Set_answer_fk0` FOREIGN KEY (`id_question`) REFERENCES `Question`(`id`);

ALTER TABLE `Selected_enum_answer` ADD CONSTRAINT `Selected_enum_answer_fk0` FOREIGN KEY (`id_session`) REFERENCES `Session`(`id`);

ALTER TABLE `Selected_enum_answer` ADD CONSTRAINT `Selected_enum_answer_fk1` FOREIGN KEY (`id_selected_enum`) REFERENCES `Enum_answer`(`id`);

ALTER TABLE `Selected_set_answer` ADD CONSTRAINT `Selected_set_answer_fk0` FOREIGN KEY (`id_session`) REFERENCES `Session`(`id`);

ALTER TABLE `Selected_set_answer` ADD CONSTRAINT `Selected_set_answer_fk1` FOREIGN KEY (`id_selected_set`) REFERENCES `Set_answer`(`id`);

ALTER TABLE `Selected_text_answer` ADD CONSTRAINT `Selected_text_answer_fk0` FOREIGN KEY (`id_session`) REFERENCES `Session`(`id`);

ALTER TABLE `Selected_text_answer` ADD CONSTRAINT `Selected_text_answer_fk1` FOREIGN KEY (`id_question`) REFERENCES `Question`(`id`);

ALTER TABLE `Session` ADD CONSTRAINT `Session_fk0` FOREIGN KEY (`id_test`) REFERENCES `Test`(`id`);
