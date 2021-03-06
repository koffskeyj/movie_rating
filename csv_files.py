import csv


def add_movie_data(apps, schema_editor):
    Movie = apps.get_model("movie_rating_relations", "Movie")
    with open("item", encoding="latin1") as infile:
        read_file = csv.reader(infile, delimiter='|')
        for row in read_file:
            Movie.objects.create(movie_id=row[0], movie_title=row[1], release_date=row[2], video_release_date=row[3], URL=row[4],
                                 unknown=row[5], Action=row[6], Adventure=row[7], Animation=row[8], Childrens=row[9], Comedy=row[10],
                                 Crime=row[11], Documentary=row[12], Drama=row[13], Fantasy=row[14], Film_Noir=row[15], Horror=row[16],
                                 Musical=row[17], Mystery=row[18], Romance=row[19], Sci_Fi=row[20], Thriller=row[21], War=row[22],
                                 Western=row[23])


def add_rater_data(apps, schema_editor):
    Rater = apps.get_model("movie_rating_relations", "Rater")
    with open("user") as infile:
        read_file = csv.reader(infile, delimiter='|')
        for row in read_file:
            Rater.objects.create(user_id=row[0], age=row[1], gender=row[2], occupation=row[3], zipcode=row[4])


def add_rating_data(apps, schema_editor):
    Rater = apps.get_model("movie_rating_relations", "Rater")
    Movie = apps.get_model("movie_rating_relations", "Movie")
    Rating = apps.get_model("movie_rating_relations", "Rating")
    with open("data") as infile:
        read_file = csv.reader(infile, delimiter='\t')
        for row in read_file:
            rater_user_id = Rater.objects.get(user_id=row[0])
            movie_movie_id = Movie.objects.get(movie_id=row[1])
            Rating.objects.create(user_id=rater_user_id, item_id=movie_movie_id, rating=row[2], time_stamp=row[3])
    raise Exception("yay")