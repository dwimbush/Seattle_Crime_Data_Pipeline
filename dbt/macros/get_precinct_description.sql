{#
    This macro returns the description of the Seattle precincts
#}

{% macro get_precinct_description(precinct) -%}
    case
        when {{ precinct }} = 'N' then 'North'
        when {{ precinct }} = 'E' then 'East'
        when {{ precinct }} = 'S' then 'South'
        when {{ precinct }} = 'W' then 'West (Downtown)'
        when {{ precinct }} = 'SW' then 'Southwest'
        else 'UNKNOWN'
    end
{%- endmacro %}
