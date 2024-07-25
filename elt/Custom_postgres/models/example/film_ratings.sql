-- Subqueries which can be referred anytime using with clause

-- Categorizing a film's rating as Excellent, Good, Average or Poor based on the user rating from the films table present in destination_db database.
with films_with_ratings as (
    select film_id, title, release_date, price, rating, user_rating, 
    case
        when user_rating >= 4.5 then 'Excellent'
        when user_rating >= 4.0 then 'Good'
        when user_rating >= 3.0 then 'Average'
        else 'Poor'
    end as rating_category
    from {{ref('films')}}
),

-- Actors of a particular film by joining the tables in destination_db
films_with_actors as (
    select f.film_id, f.title, string_agg(a.actor_name, ',') as actors
    from {{ref('films')}} f
    left join {{ref('film_actors')}} fa on f.film_id = fa.film_id
    left join {{ref('actors')}} a on fa.actor_id = a.actor_id
    group by f.film_id, f.title
)

-- The main query which categorizes actors with their ratings
select fwf.*, fwa.actors 
from films_with_ratings fwf
left join films_with_actors fwa on fwf.film_id = fwa.film_id
