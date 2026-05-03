from django.db import models

ROLE_CHOICES = [('MT', 'MT (L11 | Band 4)'), ('GET', 'GET (L08T | Band 5)')]
RATER_CHOICES = [('candidate', 'Candidate'), ('manager', 'Manager')]
OBS_CHOICES = [('30', '30 Days'), ('60', '60 Days'), ('90', '90 Days')]


class HappySheetResponse(models.Model):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    employee_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    date = models.DateField()
    program_name = models.CharField(max_length=300)
    vendor = models.CharField(max_length=200, blank=True)
    competency = models.CharField(max_length=200, blank=True)
    mode = models.CharField(max_length=100, blank=True)
    trainer = models.CharField(max_length=200, blank=True)
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    nps_score = models.IntegerField()
    open_feedback = models.TextField(blank=True)
    supervisor = models.CharField(max_length=200, blank=True)
    hr_bp = models.CharField(max_length=200, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def average_score(self):
        scores = [self.q1, self.q2, self.q3, self.q4, self.q5,
                  self.q6, self.q7, self.q8, self.q9, self.q10]
        return round(sum(scores) / 10, 2)

    def __str__(self):
        return f"{self.name} ({self.role}) — {self.date}"


class PreAssessmentResponse(models.Model):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    rater_type = models.CharField(max_length=20, choices=RATER_CHOICES)
    employee_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    role_grade = models.CharField(max_length=100, blank=True)
    dept = models.CharField(max_length=200, blank=True)
    manager_name = models.CharField(max_length=200, blank=True)
    date = models.DateField()
    competency_ratings = models.JSONField(default=dict)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} ({self.role}) [{self.rater_type}] — {self.date}"


class PostAssessmentResponse(models.Model):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    rater_type = models.CharField(max_length=20, choices=RATER_CHOICES)
    employee_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    training_completed = models.CharField(max_length=300, blank=True)
    date = models.DateField()
    manager_name = models.CharField(max_length=200, blank=True)
    days_since_training = models.IntegerField(null=True, blank=True)
    competency_ratings = models.JSONField(default=dict)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} ({self.role}) [{self.rater_type}] — {self.date}"


class BARSTechnicalResponse(models.Model):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    employee_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    obs_number = models.CharField(max_length=10, choices=OBS_CHOICES)
    period = models.CharField(max_length=100, blank=True)
    supervisor = models.CharField(max_length=200)
    date = models.DateField()
    ratings = models.JSONField(default=dict)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def average_rating(self):
        vals = [v['rating'] for v in self.ratings.values() if v.get('rating')]
        return round(sum(vals) / len(vals), 2) if vals else 0

    def __str__(self):
        return f"{self.name} ({self.role}) — {self.obs_number}d obs"


class BARSBehaviouralResponse(models.Model):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    employee_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    obs_number = models.CharField(max_length=10, choices=OBS_CHOICES)
    period = models.CharField(max_length=100, blank=True)
    supervisor = models.CharField(max_length=200)
    date = models.DateField()
    ratings = models.JSONField(default=dict)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def average_rating(self):
        vals = [v['rating'] for v in self.ratings.values() if v.get('rating')]
        return round(sum(vals) / len(vals), 2) if vals else 0

    def __str__(self):
        return f"{self.name} ({self.role}) — {self.obs_number}d obs"


class BARSLeadershipResponse(models.Model):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    employee_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    obs_number = models.CharField(max_length=10, choices=OBS_CHOICES)
    period = models.CharField(max_length=100, blank=True)
    supervisor = models.CharField(max_length=200)
    date = models.DateField()
    ratings = models.JSONField(default=dict)
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def average_rating(self):
        vals = [v['rating'] for v in self.ratings.values() if v.get('rating')]
        return round(sum(vals) / len(vals), 2) if vals else 0

    def __str__(self):
        return f"{self.name} ({self.role}) — {self.obs_number}d obs"
