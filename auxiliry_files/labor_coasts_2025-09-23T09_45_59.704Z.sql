CREATE TABLE "organizations" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"name" VARCHAR(255),
	PRIMARY KEY("id")
);




CREATE TABLE "activity_types" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"name" VARCHAR(255),
	"organization" INTEGER,
	"visible" BOOLEAN DEFAULT TRUE,
	PRIMARY KEY("id")
);




CREATE TABLE "projects" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"name" VARCHAR(255),
	"completed" BOOLEAN,
	"organization" INTEGER,
	PRIMARY KEY("id")
);




CREATE TABLE "users" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"last_name" VARCHAR(255) NOT NULL,
	"first_name" VARCHAR(255) NOT NULL,
	"patronymic" VARCHAR(255),
	"division" BIGINT NOT NULL,
	PRIMARY KEY("id")
);




CREATE TABLE "divisions" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"division" JSON,
	"organization" BIGINT NOT NULL,
	PRIMARY KEY("id")
);




CREATE TABLE "tasks" (
	"id" BIGSERIAL NOT NULL UNIQUE,
	"user" BIGINT NOT NULL,
	"project" BIGINT NOT NULL,
	"type_of_activity" BIGINT NOT NULL,
	"start_time" TIMESTAMPTZ NOT NULL,
	"end_time" TIMESTAMPTZ NOT NULL,
	"description" TEXT,
	"created_at" TIMESTAMPTZ NOT NULL DEFAULT now(),
	PRIMARY KEY("id")
);



ALTER TABLE "activity_types"
ADD FOREIGN KEY("organization") REFERENCES "organizations"("id")
ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE "projects"
ADD FOREIGN KEY("organization") REFERENCES "organizations"("id")
ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE "users"
ADD FOREIGN KEY("division") REFERENCES "divisions"("id")
ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE "divisions"
ADD FOREIGN KEY("organization") REFERENCES "organizations"("id")
ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE "tasks"
ADD FOREIGN KEY("user") REFERENCES "users"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "tasks"
ADD FOREIGN KEY("project") REFERENCES "projects"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE "tasks"
ADD FOREIGN KEY("type_of_activity") REFERENCES "activity_types"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;