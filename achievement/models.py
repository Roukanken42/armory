from django.db import models

# ACHIEVEMENT_CONFIG = (
#     ("_model", None, constant("achievement.Achievement")),
#     ("_pk", "id", int),
#     ("name", "name", ach_str),
#     ("category", "categoryId", int),
#     ("description", "description", ach_str),
#     # ("detail", "detail", optional(ach_str)),
#     ("points", "point", int),
# )

# ACHIEVEMENT_CATEGORY_CONFIG = [
#     ("_model", None, constant("achievement.Category")),
#     ("_pk", "id", int),
#     ("name", "name", ach_str),
#     ("_skip", None, constant(False)),
#     ("_skip", "isGrade", optional(bool)),
#     ("_skip", "isCompensation", optional(bool)),
#     ("_skip", "isSummary", optional(bool)),
#     ("parent", None, constant("*parent")),
#     (">subcategories", "SubCategory", optional(transform_obj(ACHIEVEMENT_SUBCATEGORY_CONFIG)))
# ]

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("Category", related_name="subcategories", null=True)

    def __str__(self):
        return self.name

    def safe(self):
        return self.name.lower().replace(" ", "-").replace("'", "")

class AchievementData(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    points = models.IntegerField()

    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    player    = models.ForeignKey("gear.Player")
    data      = models.ForeignKey(AchievementData)
    completed = models.DateTimeField()

    def __str__(self):
        return "{}: {}".format(self.player.name, self.data)