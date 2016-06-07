import csv


def movie_data(apps, schema_editor):
    Movie = apps.get_model("movie_rating_relations", "Movie")
    with open("item", encoding="latin1") as infile:
        read_file = csv.reader(infile, delimiter='|')
        for row in read_file:
            Movie.objects.create(movie_id=row[0], movie_title=row[1], release_date=row[2], video_release_date=row[3], URL=row[4],
                                 unknown=row[5], Action=row[6], Adventure=row[7], Animation=row[8], Childrens=row[9], Comedy=row[10],
                                 Crime=row[11], Documentary=row[12], Drama=row[13], Fantasy=row[14], Film_Noir=row[15], Horror=row[16],
                                 Musical=row[17], Mystery=row[18], Romance=row[19], Sci_Fi=row[20], Thriller=row[21], War=row[22],
                                 Western=row[23])
    raise Exception("yay")


def rater_data(apps, schema_editor):
    Rater = apps.get_model("movie_rating_relations", "Rater")
    with open("user") as infile:
        read_file = csv.reader(infile, delimiter='|')
        for row in read_file:
            Rater.objects.create(user_id=row[0], age=row[1], gender=row[2], occupation=row[3], zipcode=row[4])


def rating_data(apps, schema_editor):
    Rating = apps.get_model("movie_rating_relations", "Rating")
    with open("data") as infile:
        read_file = csv.reader(infile, delimiter='\t')
        for row in read_file:
            Rating.objects.create(user_id=row[0], item_id=row[1], rating=row[2], time_stamp=row[3])
