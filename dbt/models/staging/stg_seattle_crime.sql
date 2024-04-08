with 

source as (

    select * from {{ source('staging', 'seattle_crime_partitioned') }}

),

renamed as (

    select
        report_number,
        offense_id,
        offense_start_datetime,
        offense_end_datetime,
        report_datetime,
        group_a_b,
        crime_against_category,
        offense_parent_group,
        offense,
        offense_code,
        {{ get_precinct_description('precinct') }} as precinct,
        sector,
        beat,
        mcpp,
        block_address,
        longitude,
        latitude,
        pseudo_partition_date

    from source

)

select * from renamed
