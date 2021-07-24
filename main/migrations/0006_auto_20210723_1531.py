# Generated by Django 3.2.5 on 2021-07-23 19:10

from django.db import migrations

def mountain_data(apps, schema_editor):

    mountains = [
        ("Castle Peak", "14265", "Elk"),
        ("Maroon Peak", "14156", "Elk"),
        ("Capitol Peak", "14130", "Elk"),
        ("Snowmass Mountain", "14092", "Elk"),
        ("Conundrum Peak", "14060", "Elk"),
        ("Pyramid Peak", "14018", "Elk"),
        ("North Maroon Peak", "14014", "Elk"),

        ("Grays Peak", "14270", "Front"),
        ("Torreys Peak", "14267", "Front"),
        ("Mt. Evans", "14264", "Front"),
        ("Longs Peak", "14255", "Front"),
        ("Pikes Peak", "14110", "Front"),
        ("Mt. Bierstadt", "14060", "Front"),

        ("Mt. Lincoln", "14286", "Mosquito"),
        ("Mt. Cameron", "14238", "Mosquito"),
        ("Mt. Bross", "14172", "Mosquito"),
        ("Mt. Democrat", "14148", "Mosquito"),
        ("Mt. Sherman", "14036", "Mosquito"),

        ("Uncompahgre Peak", "14309", "San Juan"),
        ("Mt. Wilson", "14246", "San Juan"),
        ("El Diente Peak", "14159", "San Juan"),
        ("Mt Sneffels", "14150", "San Juan"),
        ("Windom Peak", "14087", "San Juan"),
        ("Mt Eolus", "14083", "San Juan"),
        ("Sunlight Peak", "14059", "San Juan"),
        ("Handies Peak", "14048", "San Juan"),
        ("North Eolus", "14039", "San Juan"),
        ("Redcloud Peak", "14034", "San Juan"),
        ("Wilson Peak", "14017", "San Juan"),
        ("Wetterhorn Peak", "14015", "San Juan"),
        ("San Luis Peak", "14014", "San Juan"),
        ("Sunshine Peak", "14001", "San Juan"),

        ("Blanca Peak", "14345", "Sangres"),
        ("Crestone Peak", "14294", "Sangres"),
        ("Crestone Needle", "14197", "Sangres"),
        ("Kit Carson Peak", "14165", "Sangres"),
        ("Challenger Point", "14081", "Sangres"),
        ("Humboldt Peak", "14064", "Sangres"),
        ("Culebra Peak", "14047", "Sangres"),
        ("Mt. Lindsey", "14042", "Sangres"),
        ("Ellingwood Point", "14042", "Sangres"),
        ("Little Beak Peak", "14037", "Sangres"),

        ("Mt. Elbert", "14433", "Sawatch"),
        ("Mt. Massive", "14421", "Sawatch"),
        ("Mt. Harvard", "14420", "Sawatch"),
        ("La Plata Peak", "14336", "Sawatch"),
        ("Mt. Antero", "14269", "Sawatch"),
        ("Mt. Shavano", "14229", "Sawatch"),
        ("Mt. Princeton", "14197", "Sawatch"),
        ("Mt. Belford", "14197", "Sawatch"),
        ("Mt. Yale", "14196", "Sawatch"),
        ("Tabeguache Peak", "14155", "Sawatch"),
        ("Mt. Oxford", "14153", "Sawatch"),
        ("Mt. Columbia", "14073", "Sawatch"),
        ("Missouri Mountain", "14067", "Sawatch"),
        ("Mt. of the Holy Cross", "14005", "Sawatch"),
        ("Huron Peak", "14003", "Sawatch"),

        ("Quandary Peak", "14265", "Tenmile"),
        
    ]

    Mountain = apps.get_model('main', 'Mountain')
    for m in mountains:
        mountain = Mountain()
        mountain.mountain_name = m[0]
        mountain.mountain_height = m[1]
        mountain.mountain_range = m[2]
        mountain.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210716_1650'),
    ]

    operations = [
        migrations.RunPython(mountain_data),
    ]
