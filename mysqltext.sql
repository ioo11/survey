-- МНОГО ЛИШНЕГО!!!

CREATE TABLE `Test` (
	`id` int NOT NULL,
	`id_creator` int NOT NULL,
	`name` varchar NOT NULL,
	`pub_date` DATE NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Question` (
	`id` int NOT NULL AUTO_INCREMENT,
	`id_test` int NOT NULL,
	`type` int NOT NULL,
	`text` varchar NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Enum_answer` (
	`id` int NOT NULL,
	`id_question` int NOT NULL,
	`text` varchar NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Set_answer` (
	`id` int NOT NULL,
	`id_question` int NOT NULL,
	`text` varchar NOT NULL,
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
	`answer` TEXT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Session` (
	`id` int NOT NULL,
	`id_test` int NOT NULL,
	`id_voted_user` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `User` (
	`id` int NOT NULL,
	`is_registered` bool NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Unregistered_user` (
	`id` int NOT NULL,
	`id_user` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Registered_user` (
	`id` int NOT NULL,
	`id_user` int NOT NULL,
	`fname` varchar NOT NULL,
	`lname` varchar NOT NULL,
	`sex` varchar NOT NULL,
	`age` smallint NOT NULL,
	`country` varchar NOT NULL,
	`region` varchar NOT NULL,
	`city` varchar NOT NULL,
	`reg_date` smallint NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `user_information` (
	`id` int NOT NULL,
	`id_user` int NOT NULL,
	`ip` varchar NOT NULL,
	`cookie` varchar NOT NULL,
	`date_visit` int NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Test` ADD CONSTRAINT `Test_fk0` FOREIGN KEY (`id_creator`) REFERENCES `Registered_user`(`id`);

ALTER TABLE `Question` ADD CONSTRAINT `Question_fk0` FOREIGN KEY (`id_test`) REFERENCES `Test`(`id`);

ALTER TABLE `Enum_answer` ADD CONSTRAINT `Enum_answer_fk0` FOREIGN KEY (`id_question`) REFERENCES `Question`(`id`);

ALTER TABLE `Unregistered_user` ADD CONSTRAINT `Unregistered_user_fk0` FOREIGN KEY (`id_user`) REFERENCES `User`(`id`);

ALTER TABLE `Set_answer` ADD CONSTRAINT `Set_answer_fk0` FOREIGN KEY (`id_question`) REFERENCES `Question`(`id`);

ALTER TABLE `Selected_enum_answer` ADD CONSTRAINT `Selected_enum_answer_fk0` FOREIGN KEY (`id_session`) REFERENCES `Session`(`id`);

ALTER TABLE `Selected_enum_answer` ADD CONSTRAINT `Selected_enum_answer_fk1` FOREIGN KEY (`id_selected_enum`) REFERENCES `Enum_answer`(`id`);

ALTER TABLE `Selected_set_answer` ADD CONSTRAINT `Selected_set_answer_fk0` FOREIGN KEY (`id_session`) REFERENCES `Session`(`id`);

ALTER TABLE `Selected_set_answer` ADD CONSTRAINT `Selected_set_answer_fk1` FOREIGN KEY (`id_selected_set`) REFERENCES `Set_answer`(`id`);

ALTER TABLE `Selected_text_answer` ADD CONSTRAINT `Selected_text_answer_fk0` FOREIGN KEY (`id_session`) REFERENCES `Session`(`id`);

ALTER TABLE `Selected_text_answer` ADD CONSTRAINT `Selected_text_answer_fk1` FOREIGN KEY (`id_question`) REFERENCES `Question`(`id`);

ALTER TABLE `Session` ADD CONSTRAINT `Session_fk0` FOREIGN KEY (`id_test`) REFERENCES `Test`(`id`);

ALTER TABLE `Session` ADD CONSTRAINT `Session_fk1` FOREIGN KEY (`id_voted_user`) REFERENCES `User`(`id`);

ALTER TABLE `Registered_user` ADD CONSTRAINT `Registered_user_fk0` FOREIGN KEY (`id_user`) REFERENCES `User`(`id`);

ALTER TABLE `user_information` ADD CONSTRAINT `user_information_fk0` FOREIGN KEY (`id_user`) REFERENCES `User`(`id`);

CREATE TABLE `Test` (
	`id` int NOT NULL,
	`id_creator` int NOT NULL,
	`name` varchar NOT NULL,
	`pub_date` DATE NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Question` (
	`id` int NOT NULL AUTO_INCREMENT,
	`id_test` int NOT NULL,
	`type` int NOT NULL,
	`text` varchar NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Enum_answer` (
	`id` int NOT NULL,
	`id_question` int NOT NULL,
	`text` varchar NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Set_answer` (
	`id` int NOT NULL,
	`id_question` int NOT NULL,
	`text` varchar NOT NULL,
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
	`answer` TEXT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Session` (
	`id` int NOT NULL,
	`id_test` int NOT NULL,
	`id_voted_user` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `User` (
	`id` int NOT NULL,
	`is_registered` bool NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Unregistered_user` (
	`id` int NOT NULL,
	`id_user` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Registered_user` (
	`id` int NOT NULL,
	`id_user` int NOT NULL,
	`fname` varchar NOT NULL,
	`lname` varchar NOT NULL,
	`sex` varchar NOT NULL,
	`age` smallint NOT NULL,
	`country` varchar NOT NULL,
	`region` varchar NOT NULL,
	`city` varchar NOT NULL,
	`reg_date` smallint NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `user_information` (
	`id` int NOT NULL,
	`id_user` int NOT NULL,
	`ip` varchar NOT NULL,
	`cookie` varchar NOT NULL,
	`date_visit` int NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Test` ADD CONSTRAINT `Test_fk0` FOREIGN KEY (`id_creator`) REFERENCES `Registered_user`(`id`);

ALTER TABLE `Question` ADD CONSTRAINT `Question_fk0` FOREIGN KEY (`id_test`) REFERENCES `Test`(`id`);

ALTER TABLE `Enum_answer` ADD CONSTRAINT `Enum_answer_fk0` FOREIGN KEY (`id_question`) REFERENCES `Question`(`id`);

ALTER TABLE `Unregistered_user` ADD CONSTRAINT `Unregistered_user_fk0` FOREIGN KEY (`id_user`) REFERENCES `User`(`id`);

ALTER TABLE `Set_answer` ADD CONSTRAINT `Set_answer_fk0` FOREIGN KEY (`id_question`) REFERENCES `Question`(`id`);

ALTER TABLE `Selected_enum_answer` ADD CONSTRAINT `Selected_enum_answer_fk0` FOREIGN KEY (`id_session`) REFERENCES `Session`(`id`);

ALTER TABLE `Selected_enum_answer` ADD CONSTRAINT `Selected_enum_answer_fk1` FOREIGN KEY (`id_selected_enum`) REFERENCES `Enum_answer`(`id`);

ALTER TABLE `Selected_set_answer` ADD CONSTRAINT `Selected_set_answer_fk0` FOREIGN KEY (`id_session`) REFERENCES `Session`(`id`);

ALTER TABLE `Selected_set_answer` ADD CONSTRAINT `Selected_set_answer_fk1` FOREIGN KEY (`id_selected_set`) REFERENCES `Set_answer`(`id`);

ALTER TABLE `Selected_text_answer` ADD CONSTRAINT `Selected_text_answer_fk0` FOREIGN KEY (`id_session`) REFERENCES `Session`(`id`);

ALTER TABLE `Selected_text_answer` ADD CONSTRAINT `Selected_text_answer_fk1` FOREIGN KEY (`id_question`) REFERENCES `Question`(`id`);

ALTER TABLE `Session` ADD CONSTRAINT `Session_fk0` FOREIGN KEY (`id_test`) REFERENCES `Test`(`id`);

ALTER TABLE `Session` ADD CONSTRAINT `Session_fk1` FOREIGN KEY (`id_voted_user`) REFERENCES `User`(`id`);

ALTER TABLE `Registered_user` ADD CONSTRAINT `Registered_user_fk0` FOREIGN KEY (`id_user`) REFERENCES `User`(`id`);

ALTER TABLE `user_information` ADD CONSTRAINT `user_information_fk0` FOREIGN KEY (`id_user`) REFERENCES `User`(`id`);
