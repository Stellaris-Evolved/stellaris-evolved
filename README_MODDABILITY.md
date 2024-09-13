# Evolved Moddability and Extension

Stellaris Evolved supports internally a way of extending existing inlines and triggers 
without needing to overwrite Evolved defined files.

## Setup on your side of the mod

Create a scripted variable in `common/scripted_variables` folder in a file with `!!` prefix. You will have
to create a variable with your `suffix` in it like below.

```
@tec_<suffix>_addon_present = 1
```

## How to identify what can be extended

### Scripted triggers and effects

Scripted triggers that have an inline_script called in them like `mod_support/tec_trigger_include`, and scripted effects 
that have the  `mod_support/tec_effect_include` or script value that have `mod_support/tec_value_include`
inside their logic, usually inside an `OR` statement can be extended by creating a scripted trigger
of your own with a suffix appended to the trigger/effect name.

For example, if you want to add a spiritualist main cult, and have it supported
by automatically disabling normal temples and swapping you priest, you might want
to overwrite the `tec_is_spiritualist_main_cult`. But with the extension mechanism
we have in place you can create `tec_is_spiritualist_main_cult_<suffix>` the `<suffix>`
being a specific identifier that we can create and add to evolved for your 
patch/mod/addon etc.

IE, something like below, if your `<suffix>` is `sam`:

```
tec_is_spiritualist_main_cult_sam = {
    OR = {
        has_valid_civic = civic_sam_my_cult_civic
    }
}
```

A list of all available suffixes will be available below.

### Inline scripts

Inline scripts that have `mod_support/tec_inlines_include` inside their logic
allow themselves to be extended by creating an inline inside the `common/inline_scripts/evolved_support`
with the path of the inline you want to extend.

For example if we want to extend as above the main cult swaps of priests,
you will want to extend the `jobs/tec_priest` inline, which you can do by making
a file at the path `common/inline_scripts/evolved_support/jobs/tec_priest_<suffix>`, the `<suffix>`
being a specific identifier that we can create and add to evolved for your patch/mod/addon etc.

All parameters of the extended inline will be available in your inline too.

IE, something like below, if your `<suffix>` is `sam`:

```
# file: common/inline_scripts/evolved_support/jobs/tec_priest_sam.txt

inline_script = {	
    script = jobs/tec_job
    trigger = "
        exists = owner

        $trigger$

        owner = {
            has_valid_civic = civic_sam_my_cult_civic
        }
    "
    job = sam_my_cult_priest
    count = $count$
    mult = $mult$
    display = $display$
}
```
## Current suffixes

* giga_patch
* pd_patch
* serente
* kes
* modded_other
* tec_experimental

## Current supported scripted_triggers

* [has_ringworld_output_boost](common/scripted_triggers/zzzz_ow_00_scripted_triggers.txt#L313)
* [tec_allows_machine_alt_capitals](common/scripted_triggers/zzz_evolved_buildings_scripted_triggers.txt#L2060)
* [tec_blocks_industrial_designations](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L5126)
* [tec_blocks_non_industrial_designations](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L5146)
* [tec_blocks_regular_designations](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L5073)
* [tec_blocks_rural_designations](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L5107)
* [tec_blocks_urban_designations](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L5086)
* [tec_country_has_autocratic_authority](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1756)
* [tec_country_has_democratic_authority](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1735)
* [tec_country_has_oligarchic_authority](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1745)
* [tec_has_amenity_building_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L633)
* [tec_has_artisan_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L416)
* [tec_has_artisan_upkeep_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L537)
* [tec_has_artisan_upkeep_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L527)
* [tec_has_bureaucratic_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L433)
* [tec_has_clerk_job](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3581)
* [tec_has_clerk_jobs_available](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3570)
* [tec_has_clerk_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L100)
* [tec_has_clerk_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L85)
* [tec_has_clinic_building_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L229)
* [tec_has_colonist_half_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L69)
* [tec_has_colonist_half_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L54)
* [tec_has_colonist_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L39)
* [tec_has_coordinator_job](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3644)
* [tec_has_coordinator_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L117)
* [tec_has_crime_job](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3551)
* [tec_has_crime_jobs_available](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3524)
* [tec_has_cyborg_clinic_exception](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L245)
* [tec_has_diplomatic_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1167)
* [tec_has_directive_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L604)
* [tec_has_enforcer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L23)
* [tec_has_entertainer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L7)
* [tec_has_farmer_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L276)
* [tec_has_farmer_production_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L558)
* [tec_has_farmer_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L547)
* [tec_has_farmer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L257)
* [tec_has_forced_living_standard_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L648)
* [tec_has_foundry_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L400)
* [tec_has_foundry_upkeep_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L517)
* [tec_has_foundry_upkeep_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L504)
* [tec_has_healthcare_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L212)
* [tec_has_housing_building_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L622)
* [tec_has_maintenance_drone_job](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3607)
* [tec_has_maintenance_drone_jobs_available](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3592)
* [tec_has_maintenance_drone_swap_civic_hive](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L563)
* [tec_has_maintenance_drone_swap_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L631)
* [tec_has_maintenance_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L166)
* [tec_has_matter_miner](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L346)
* [tec_has_miner_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L311)
* [tec_has_miner_production_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L579)
* [tec_has_miner_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L568)
* [tec_has_miner_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L293)
* [tec_has_monument_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L458)
* [tec_has_naval_academy_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L493)
* [tec_has_orbital_energy_deposit](common/scripted_triggers/zzz_evolved_galaxy_gen_scripted_triggers.txt#L81)
* [tec_has_orbital_engineering_deposit](common/scripted_triggers/zzz_evolved_galaxy_gen_scripted_triggers.txt#L21)
* [tec_has_orbital_food_deposit](common/scripted_triggers/zzz_evolved_galaxy_gen_scripted_triggers.txt#L54)
* [tec_has_orbital_mining_deposit](common/scripted_triggers/zzz_evolved_galaxy_gen_scripted_triggers.txt#L96)
* [tec_has_orbital_physics_deposit](common/scripted_triggers/zzz_evolved_galaxy_gen_scripted_triggers.txt#L4)
* [tec_has_orbital_society_deposit](common/scripted_triggers/zzz_evolved_galaxy_gen_scripted_triggers.txt#L38)
* [tec_has_patrol_drone_job](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3654)
* [tec_has_patrol_drone_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L181)
* [tec_has_priest_job](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3664)
* [tec_has_research_job](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3691)
* [tec_has_research_lab_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L470)
* [tec_has_ruler_civic_hive](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L540)
* [tec_has_ruler_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L579)
* [tec_has_ruler_civic_mega](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L512)
* [tec_has_ruler_civic_regular](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L425)
* [tec_has_ruler_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L654)
* [tec_has_scrap_miner](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L581)
* [tec_has_slaver_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1143)
* [tec_has_soldier_job](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3762)
* [tec_has_soldier_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L150)
* [tec_has_soldier_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L133)
* [tec_has_special_ruler_feature](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L380)
* [tec_has_spy_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1157)
* [tec_has_standard_habitation_district](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L2315)
* [tec_has_standard_habitation_district_block](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L2359)
* [tec_has_standard_industrial_district](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L2376)
* [tec_has_standard_industrial_district_block](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L2413)
* [tec_has_stronghold_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L481)
* [tec_has_synapse_job](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L3632)
* [tec_has_t1_assembly_building](common/scripted_triggers/zzz_evolved_buildings_scripted_triggers.txt#L1844)
* [tec_has_t2_assembly_building](common/scripted_triggers/zzz_evolved_buildings_scripted_triggers.txt#L1861)
* [tec_has_t3_assembly_building](common/scripted_triggers/zzz_evolved_buildings_scripted_triggers.txt#L1878)
* [tec_has_technician_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L384)
* [tec_has_technician_production_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L602)
* [tec_has_technician_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L591)
* [tec_has_technician_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L366)
* [tec_has_temple_swap_exception](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L611)
* [tec_has_warrior_drone_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L196)
* [tec_invalidates_assembly_buildings](common/scripted_triggers/zzz_evolved_buildings_scripted_triggers.txt#L1829)
* [tec_is_arcology](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L1670)
* [tec_is_city_world](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L1789)
* [tec_is_elysium](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L1765)
* [tec_is_habitat](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L1707)
* [tec_is_modded_space_arcology](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L1612)
* [tec_is_ringworld](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L1742)
* [tec_is_space_arcology](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L1688)
* [tec_is_special_researcher_empire](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L161)
* [tec_is_spiritualist_main_cult](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L333)
* [tec_is_spiritualist_secondary_cult](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L356)
* [tec_is_subhabitat_megastructure](common/scripted_triggers/zzz_evolved_galaxy_gen_scripted_triggers.txt#L115)
* [tec_is_wet_modded_planet_exceptions](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L1939)
* [tec_planet_special_blocks_assembly_buildings](common/scripted_triggers/zzz_evolved_buildings_scripted_triggers.txt#L1816)
* [tec_replaces_half_researcher_empire](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L184)
* [tec_uses_elysium_districts](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L1845)
* [tec_uses_habitat_districts](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L1811)
* [tec_uses_ringworld_districts](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L1822)

## Current supported scripted_effects

* [tec_cache_building_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L415)
* [tec_cache_capital_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L414)
* [tec_cache_colony_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L416)
* [tec_cache_combined_values](common/scripted_effects/zz_evolved_scripted_effects.txt#L417)
* [tec_cache_country_civic_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L712)
* [tec_cache_country_monthly_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L614)
* [tec_cache_planet_type_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L413)
* [tec_cache_pop_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L460)
* [tec_cache_species_traits_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L565)
* [tec_on_subhabitat_complete_effect](common/scripted_effects/zz_evolved_arcology_scripted_effects.txt#L535)

## Current supported scripted_effects

* [crystals_buildings_value](common/script_values/zz_evolved_script_values.txt#L1461)
* [farming_buildings_value](common/script_values/zz_evolved_script_values.txt#L1182)
* [farming_combined_value](common/script_values/zz_evolved_script_values.txt#L1760)
* [farming_districts_value](common/script_values/zz_evolved_script_values.txt#L453)
* [gases_buildings_value](common/script_values/zz_evolved_script_values.txt#L1508)
* [generator_buildings_value](common/script_values/zz_evolved_script_values.txt#L1295)
* [generator_combined_value](common/script_values/zz_evolved_script_values.txt#L1820)
* [generator_districts_value](common/script_values/zz_evolved_script_values.txt#L567)
* [housing_districts_value](common/script_values/zz_evolved_script_values.txt#L849)
* [industrial_districts_value](common/script_values/zz_evolved_script_values.txt#L637)
* [leisure_district_value](common/script_values/zz_evolved_script_values.txt#L1134)
* [military_combined_value](common/script_values/zz_evolved_script_values.txt#L2002)
* [mining_buildings_value](common/script_values/zz_evolved_script_values.txt#L1246)
* [mining_combined_value](common/script_values/zz_evolved_script_values.txt#L1790)
* [mining_districts_value](common/script_values/zz_evolved_script_values.txt#L510)
* [motes_buildings_value](common/script_values/zz_evolved_script_values.txt#L1413)
* [refinery_combined_value](common/script_values/zz_evolved_script_values.txt#L1911)
* [research_buildings_value](common/script_values/zz_evolved_script_values.txt#L1346)
* [research_combined_value](common/script_values/zz_evolved_script_values.txt#L1850)
* [research_districts_value](common/script_values/zz_evolved_script_values.txt#L773)
* [stronghold_buildings_value](common/script_values/zz_evolved_script_values.txt#L1555)
* [tec_district_farming_max_value](common/script_values/zz_evolved_script_values.txt#L2381)
* [tec_district_generator_max_value](common/script_values/zz_evolved_script_values.txt#L2443)
* [tec_district_mining_max_value](common/script_values/zz_evolved_script_values.txt#L2412)
* [tec_farmer_jobs_value](common/script_values/zz_evolved_script_values.txt#L2357)
* [tec_priest_jobs_value](common/script_values/zz_evolved_script_values.txt#L2250)
* [tec_researcher_jobs_value](common/script_values/zz_evolved_script_values.txt#L2170)
* [tec_soldier_jobs_value](common/script_values/zz_evolved_script_values.txt#L2290)
* [tec_trader_jobs_value](common/script_values/zz_evolved_script_values.txt#L2334)
* [trade_building_value](common/script_values/zz_evolved_script_values.txt#L1731)
* [trade_combined_value](common/script_values/zz_evolved_script_values.txt#L1973)
* [trade_districts_value](common/script_values/zz_evolved_script_values.txt#L1088)
* [unity_buildings_value](common/script_values/zz_evolved_script_values.txt#L1615)
* [unity_combined_value](common/script_values/zz_evolved_script_values.txt#L1880)
* [unity_districts_value](common/script_values/zz_evolved_script_values.txt#L950)
* [unity_servitor_specific_districts_value](common/script_values/zz_evolved_script_values.txt#L1042)
* [virtuality_concentrated_production_mult](common/script_values/zz_ow_04_script_values_machine_age.txt#L3)
* [virtuality_num_colonies](common/script_values/zz_ow_04_script_values_machine_age.txt#L29)

## Current supported inline_scripts

* [buildings/convert_to/tec_amenities_1](common/inline_scripts/buildings/convert_to/tec_amenities_1.txt#L10)
* [buildings/convert_to/tec_amenities_2](common/inline_scripts/buildings/convert_to/tec_amenities_2.txt#L10)
* [buildings/convert_to/tec_assembly_bioservant_1](common/inline_scripts/buildings/convert_to/tec_assembly_bioservant_1.txt#L11)
* [buildings/convert_to/tec_assembly_bioservant_2](common/inline_scripts/buildings/convert_to/tec_assembly_bioservant_2.txt#L11)
* [buildings/convert_to/tec_assembly_bioservant_3](common/inline_scripts/buildings/convert_to/tec_assembly_bioservant_3.txt#L11)
* [buildings/convert_to/tec_assembly_organic_1](common/inline_scripts/buildings/convert_to/tec_assembly_organic_1.txt#L16)
* [buildings/convert_to/tec_assembly_organic_2](common/inline_scripts/buildings/convert_to/tec_assembly_organic_2.txt#L16)
* [buildings/convert_to/tec_assembly_organic_3](common/inline_scripts/buildings/convert_to/tec_assembly_organic_3.txt#L16)
* [buildings/convert_to/tec_assembly_robotic_1](common/inline_scripts/buildings/convert_to/tec_assembly_robotic_1.txt#L16)
* [buildings/convert_to/tec_assembly_robotic_2](common/inline_scripts/buildings/convert_to/tec_assembly_robotic_2.txt#L16)
* [buildings/convert_to/tec_assembly_robotic_3](common/inline_scripts/buildings/convert_to/tec_assembly_robotic_3.txt#L16)
* [buildings/convert_to/tec_bureaucratic_1](common/inline_scripts/buildings/convert_to/tec_bureaucratic_1.txt#L24)
* [buildings/convert_to/tec_bureaucratic_2](common/inline_scripts/buildings/convert_to/tec_bureaucratic_2.txt#L24)
* [buildings/convert_to/tec_bureaucratic_3](common/inline_scripts/buildings/convert_to/tec_bureaucratic_3.txt#L24)
* [buildings/convert_to/tec_capital_t1](common/inline_scripts/buildings/convert_to/tec_capital_t1.txt#L12)
* [buildings/convert_to/tec_capital_t2](common/inline_scripts/buildings/convert_to/tec_capital_t2.txt#L13)
* [buildings/convert_to/tec_capital_t3](common/inline_scripts/buildings/convert_to/tec_capital_t3.txt#L12)
* [buildings/convert_to/tec_capital_t4](common/inline_scripts/buildings/convert_to/tec_capital_t4.txt#L13)
* [buildings/convert_to/tec_capital_t5](common/inline_scripts/buildings/convert_to/tec_capital_t5.txt#L14)
* [buildings/convert_to/tec_clinic_1](common/inline_scripts/buildings/convert_to/tec_clinic_1.txt#L12)
* [buildings/convert_to/tec_clinic_2](common/inline_scripts/buildings/convert_to/tec_clinic_2.txt#L12)
* [buildings/convert_to/tec_clinic_3](common/inline_scripts/buildings/convert_to/tec_clinic_3.txt#L12)
* [buildings/convert_to/tec_crime_1](common/inline_scripts/buildings/convert_to/tec_crime_1.txt#L15)
* [buildings/convert_to/tec_crime_2](common/inline_scripts/buildings/convert_to/tec_crime_2.txt#L14)
* [buildings/convert_to/tec_housing_1](common/inline_scripts/buildings/convert_to/tec_housing_1.txt#L19)
* [buildings/convert_to/tec_housing_2](common/inline_scripts/buildings/convert_to/tec_housing_2.txt#L20)
* [buildings/convert_to/tec_monument_1](common/inline_scripts/buildings/convert_to/tec_monument_1.txt#L14)
* [buildings/convert_to/tec_monument_2](common/inline_scripts/buildings/convert_to/tec_monument_2.txt#L14)
* [buildings/convert_to/tec_monument_3](common/inline_scripts/buildings/convert_to/tec_monument_3.txt#L14)
* [buildings/convert_to/tec_naval_academy_1](common/inline_scripts/buildings/convert_to/tec_naval_academy_1.txt#L12)
* [buildings/convert_to/tec_naval_academy_2](common/inline_scripts/buildings/convert_to/tec_naval_academy_2.txt#L12)
* [buildings/convert_to/tec_naval_academy_3](common/inline_scripts/buildings/convert_to/tec_naval_academy_3.txt#L12)
* [buildings/convert_to/tec_research_1](common/inline_scripts/buildings/convert_to/tec_research_1.txt#L16)
* [buildings/convert_to/tec_research_2](common/inline_scripts/buildings/convert_to/tec_research_2.txt#L16)
* [buildings/convert_to/tec_research_3](common/inline_scripts/buildings/convert_to/tec_research_3.txt#L16)
* [buildings/convert_to/tec_stronghold_1](common/inline_scripts/buildings/convert_to/tec_stronghold_1.txt#L12)
* [buildings/convert_to/tec_stronghold_2](common/inline_scripts/buildings/convert_to/tec_stronghold_2.txt#L12)
* [buildings/convert_to/tec_stronghold_3](common/inline_scripts/buildings/convert_to/tec_stronghold_3.txt#L12)
* [buildings/convert_to/tec_temple_1](common/inline_scripts/buildings/convert_to/tec_temple_1.txt#L24)
* [buildings/convert_to/tec_temple_2](common/inline_scripts/buildings/convert_to/tec_temple_2.txt#L24)
* [buildings/convert_to/tec_temple_3](common/inline_scripts/buildings/convert_to/tec_temple_3.txt#L24)
* [buildings/convert_to/tec_trade_1](common/inline_scripts/buildings/convert_to/tec_trade_1.txt#L10)
* [buildings/convert_to/tec_trade_2](common/inline_scripts/buildings/convert_to/tec_trade_2.txt#L10)
* [buildings/effects/type/tec_amenities](common/inline_scripts/buildings/effects/type/tec_amenities.txt#L16)
* [buildings/effects/type/tec_amenities_hive](common/inline_scripts/buildings/effects/type/tec_amenities_hive.txt#L5)
* [buildings/effects/type/tec_amenities_machine](common/inline_scripts/buildings/effects/type/tec_amenities_machine.txt#L5)
* [buildings/effects/type/tec_amenities_regular](common/inline_scripts/buildings/effects/type/tec_amenities_regular.txt#L5)
* [buildings/effects/type/tec_bureaucratic](common/inline_scripts/buildings/effects/type/tec_bureaucratic.txt#L23)
* [buildings/effects/type/tec_bureaucratic_hive](common/inline_scripts/buildings/effects/type/tec_bureaucratic_hive.txt#L14)
* [buildings/effects/type/tec_bureaucratic_machine](common/inline_scripts/buildings/effects/type/tec_bureaucratic_machine.txt#L5)
* [buildings/effects/type/tec_bureaucratic_regular](common/inline_scripts/buildings/effects/type/tec_bureaucratic_regular.txt#L19)
* [buildings/effects/type/tec_chemical_plant](common/inline_scripts/buildings/effects/type/tec_chemical_plant.txt#L10)
* [buildings/effects/type/tec_cloning](common/inline_scripts/buildings/effects/type/tec_cloning.txt#L35)
* [buildings/effects/type/tec_cloning_hive](common/inline_scripts/buildings/effects/type/tec_cloning_hive.txt#L10)
* [buildings/effects/type/tec_cloning_machine](common/inline_scripts/buildings/effects/type/tec_cloning_machine.txt#L10)
* [buildings/effects/type/tec_cloning_regular](common/inline_scripts/buildings/effects/type/tec_cloning_regular.txt#L10)
* [buildings/effects/type/tec_crystal_plant](common/inline_scripts/buildings/effects/type/tec_crystal_plant.txt#L10)
* [buildings/effects/type/tec_energrid](common/inline_scripts/buildings/effects/type/tec_energrid.txt#L10)
* [buildings/effects/type/tec_energy_grid](common/inline_scripts/buildings/effects/type/tec_energy_grid.txt#L84)
* [buildings/effects/type/tec_factory](common/inline_scripts/buildings/effects/type/tec_factory.txt#L10)
* [buildings/effects/type/tec_food_processing_facility](common/inline_scripts/buildings/effects/type/tec_food_processing_facility.txt#L86)
* [buildings/effects/type/tec_fortress](common/inline_scripts/buildings/effects/type/tec_fortress.txt#L16)
* [buildings/effects/type/tec_fortress_hive](common/inline_scripts/buildings/effects/type/tec_fortress_hive.txt#L5)
* [buildings/effects/type/tec_fortress_machine](common/inline_scripts/buildings/effects/type/tec_fortress_machine.txt#L5)
* [buildings/effects/type/tec_fortress_regular](common/inline_scripts/buildings/effects/type/tec_fortress_regular.txt#L7)
* [buildings/effects/type/tec_foundry](common/inline_scripts/buildings/effects/type/tec_foundry.txt#L30)
* [buildings/effects/type/tec_healthcare](common/inline_scripts/buildings/effects/type/tec_healthcare.txt#L31)
* [buildings/effects/type/tec_hydroponics_farm](common/inline_scripts/buildings/effects/type/tec_hydroponics_farm.txt#L10)
* [buildings/effects/type/tec_military_booster](common/inline_scripts/buildings/effects/type/tec_military_booster.txt#L8)
* [buildings/effects/type/tec_mineral_purification_plant](common/inline_scripts/buildings/effects/type/tec_mineral_purification_plant.txt#L69)
* [buildings/effects/type/tec_ministry_production](common/inline_scripts/buildings/effects/type/tec_ministry_production.txt#L5)
* [buildings/effects/type/tec_monument](common/inline_scripts/buildings/effects/type/tec_monument.txt#L16)
* [buildings/effects/type/tec_monument_hive](common/inline_scripts/buildings/effects/type/tec_monument_hive.txt#L6)
* [buildings/effects/type/tec_monument_machine](common/inline_scripts/buildings/effects/type/tec_monument_machine.txt#L6)
* [buildings/effects/type/tec_monument_regular](common/inline_scripts/buildings/effects/type/tec_monument_regular.txt#L5)
* [buildings/effects/type/tec_naval_academy](common/inline_scripts/buildings/effects/type/tec_naval_academy.txt#L16)
* [buildings/effects/type/tec_naval_academy_hive](common/inline_scripts/buildings/effects/type/tec_naval_academy_hive.txt#L5)
* [buildings/effects/type/tec_naval_academy_machine](common/inline_scripts/buildings/effects/type/tec_naval_academy_machine.txt#L5)
* [buildings/effects/type/tec_naval_academy_regular](common/inline_scripts/buildings/effects/type/tec_naval_academy_regular.txt#L7)
* [buildings/effects/type/tec_refinery](common/inline_scripts/buildings/effects/type/tec_refinery.txt#L10)
* [buildings/effects/type/tec_research_booster](common/inline_scripts/buildings/effects/type/tec_research_booster.txt#L26)
* [buildings/effects/type/tec_research_lab](common/inline_scripts/buildings/effects/type/tec_research_lab.txt#L38)
* [buildings/effects/type/tec_research_lab_hive](common/inline_scripts/buildings/effects/type/tec_research_lab_hive.txt#L5)
* [buildings/effects/type/tec_research_lab_machine](common/inline_scripts/buildings/effects/type/tec_research_lab_machine.txt#L6)
* [buildings/effects/type/tec_research_lab_regular](common/inline_scripts/buildings/effects/type/tec_research_lab_regular.txt#L16)
* [buildings/effects/type/tec_resource_silo](common/inline_scripts/buildings/effects/type/tec_resource_silo.txt#L15)
* [buildings/effects/type/tec_robot_assembly](common/inline_scripts/buildings/effects/type/tec_robot_assembly.txt#L23)
* [buildings/effects/type/tec_robot_assembly_hive](common/inline_scripts/buildings/effects/type/tec_robot_assembly_hive.txt#L10)
* [buildings/effects/type/tec_robot_assembly_machine](common/inline_scripts/buildings/effects/type/tec_robot_assembly_machine.txt#L10)
* [buildings/effects/type/tec_robot_assembly_regular](common/inline_scripts/buildings/effects/type/tec_robot_assembly_regular.txt#L18)
* [buildings/effects/type/tec_strategic_optimizer](common/inline_scripts/buildings/effects/type/tec_strategic_optimizer.txt#L5)
* [buildings/effects/type/tec_stripmine](common/inline_scripts/buildings/effects/type/tec_stripmine.txt#L10)
* [buildings/effects/type/tec_temple](common/inline_scripts/buildings/effects/type/tec_temple.txt#L20)
* [buildings/effects/type/tec_trade](common/inline_scripts/buildings/effects/type/tec_trade.txt#L22)
* [buildings/effects/type/tec_trade_hive](common/inline_scripts/buildings/effects/type/tec_trade_hive.txt#L5)
* [buildings/effects/type/tec_trade_machine](common/inline_scripts/buildings/effects/type/tec_trade_machine.txt#L5)
* [buildings/effects/type/tec_trade_regular](common/inline_scripts/buildings/effects/type/tec_trade_regular.txt#L16)
* [buildings/effects/type/tec_unity_booster](common/inline_scripts/buildings/effects/type/tec_unity_booster.txt#L9)
* [capitals/tec_all_capital](common/inline_scripts/capitals/tec_all_capital.txt#L159)
* [capitals/tec_colony](common/inline_scripts/capitals/tec_colony.txt#L13)
* [capitals/tec_colony_habitat](common/inline_scripts/capitals/tec_colony_habitat.txt#L14)
* [capitals/tec_common_habitat_modifiers](common/inline_scripts/capitals/tec_common_habitat_modifiers.txt#L89)
* [capitals/tec_common_modifiers](common/inline_scripts/capitals/tec_common_modifiers.txt#L13)
* [capitals/tec_hive_capital](common/inline_scripts/capitals/tec_hive_capital.txt#L126)
* [capitals/tec_machine_capital](common/inline_scripts/capitals/tec_machine_capital.txt#L102)
* [capitals/tec_regular_capital](common/inline_scripts/capitals/tec_regular_capital.txt#L150)
* [capitals/tec_special_capital](common/inline_scripts/capitals/tec_special_capital.txt#L32)
* [districts/convert_to/tec_factory_districts](common/inline_scripts/districts/convert_to/tec_factory_districts.txt#L10)
* [districts/convert_to/tec_farming_districts](common/inline_scripts/districts/convert_to/tec_farming_districts.txt#L11)
* [districts/convert_to/tec_generator_districts](common/inline_scripts/districts/convert_to/tec_generator_districts.txt#L10)
* [districts/convert_to/tec_housing_districts](common/inline_scripts/districts/convert_to/tec_housing_districts.txt#L10)
* [districts/convert_to/tec_industrial_districts](common/inline_scripts/districts/convert_to/tec_industrial_districts.txt#L10)
* [districts/convert_to/tec_leisure_districts](common/inline_scripts/districts/convert_to/tec_leisure_districts.txt#L11)
* [districts/convert_to/tec_mining_districts](common/inline_scripts/districts/convert_to/tec_mining_districts.txt#L12)
* [districts/convert_to/tec_research_districts](common/inline_scripts/districts/convert_to/tec_research_districts.txt#L11)
* [districts/convert_to/tec_trade_districts](common/inline_scripts/districts/convert_to/tec_trade_districts.txt#L10)
* [districts/convert_to/tec_unity_districts](common/inline_scripts/districts/convert_to/tec_unity_districts.txt#L11)
* [districts/type/tec_housing_arcology](common/inline_scripts/districts/type/tec_housing_arcology.txt#L36)
* [districts/type/tec_housing_city](common/inline_scripts/districts/type/tec_housing_city.txt#L23)
* [districts/type/tec_housing_generic](common/inline_scripts/districts/type/tec_housing_generic.txt#L20)
* [districts/type/tec_housing_habitat](common/inline_scripts/districts/type/tec_housing_habitat.txt#L49)
* [districts/type/tec_housing_hive](common/inline_scripts/districts/type/tec_housing_hive.txt#L24)
* [districts/type/tec_housing_nexus](common/inline_scripts/districts/type/tec_housing_nexus.txt#L35)
* [districts/type/tec_industrial](common/inline_scripts/districts/type/tec_industrial.txt#L22)
* [districts/type/tec_maintenance](common/inline_scripts/districts/type/tec_maintenance.txt#L20)
* [districts/type/tec_research](common/inline_scripts/districts/type/tec_research.txt#L22)
* [districts/type/tec_rural_farming](common/inline_scripts/districts/type/tec_rural_farming.txt#L94)
* [districts/type/tec_rural_generator](common/inline_scripts/districts/type/tec_rural_generator.txt#L90)
* [districts/type/tec_rural_mining](common/inline_scripts/districts/type/tec_rural_mining.txt#L92)
* [districts/type/tec_trade](common/inline_scripts/districts/type/tec_trade.txt#L45)
* [districts/type/tec_unity](common/inline_scripts/districts/type/tec_unity.txt#L22)
* [governments/authorities/tec_auth_corporate_swap](common/governments/authorities/00_authorities.txt#L874)
* [governments/authorities/tec_auth_democratic_swap](common/governments/authorities/00_authorities.txt#L78)
* [governments/authorities/tec_auth_dictatorial_swap](common/governments/authorities/00_authorities.txt#L501)
* [governments/authorities/tec_auth_hive_mind_swap](common/governments/authorities/00_authorities.txt#L1229)
* [governments/authorities/tec_auth_imperial_swap](common/governments/authorities/00_authorities.txt#L729)
* [governments/authorities/tec_auth_machine_intelligence_swap](common/governments/authorities/00_authorities.txt#L1517)
* [governments/authorities/tec_auth_oligarchic_swap](common/governments/authorities/00_authorities.txt#L302)
* [governments/authorities/tec_auth_tec_ai_corporate_swap](common/governments/authorities/00_authorities.txt#L1160)
* [governments/authorities/tec_auth_tec_ai_swap](common/governments/authorities/00_authorities.txt#L1094)
* [governments/authorities/tec_auth_tec_hive_biological_swap](common/governments/authorities/00_authorities.txt#L1325)
* [governments/authorities/tec_auth_tec_hive_biomechanical_swap](common/governments/authorities/00_authorities.txt#L1451)
* [governments/authorities/tec_auth_tec_hive_cybernetic_swap](common/governments/authorities/00_authorities.txt#L1391)
* [governments/authorities/tec_auth_tec_machine_consensus_swap](common/governments/authorities/00_authorities.txt#L1632)
* [governments/authorities/tec_auth_tec_patrocorporate_swap](common/governments/authorities/00_authorities.txt#L1019)
* [governments/authorities/tec_auth_tec_theocracy_swap](common/governments/authorities/00_authorities.txt#L438)
* [jobs/capital/tec_add_job_civic_hive](common/inline_scripts/jobs/capital/tec_add_job_civic_hive.txt#L25)
* [jobs/capital/tec_add_job_civic_machine](common/inline_scripts/jobs/capital/tec_add_job_civic_machine.txt#L25)
* [jobs/capital/tec_add_job_civic_regular](common/inline_scripts/jobs/capital/tec_add_job_civic_regular.txt#L152)
* [jobs/capital/tec_add_job_per_ascension_civic_hive](common/inline_scripts/jobs/capital/tec_add_job_per_ascension_civic_hive.txt#L58)
* [jobs/capital/tec_add_job_per_ascension_civic_machine](common/inline_scripts/jobs/capital/tec_add_job_per_ascension_civic_machine.txt#L22)
* [jobs/capital/tec_add_job_per_ascension_civic_regular](common/inline_scripts/jobs/capital/tec_add_job_per_ascension_civic_regular.txt#L5)
* [jobs/capital/tec_add_ruler_civic_regular](common/inline_scripts/jobs/capital/tec_add_ruler_civic_regular.txt#L111)
* [jobs/effects/type/tec_administrator_effect](common/inline_scripts/jobs/effects/type/tec_administrator_effect.txt#L13)
* [jobs/effects/type/tec_agri_drone_effect](common/inline_scripts/jobs/effects/type/tec_agri_drone_effect.txt#L16)
* [jobs/effects/type/tec_artisan_effect](common/inline_scripts/jobs/effects/type/tec_artisan_effect.txt#L5)
* [jobs/effects/type/tec_brain_drone_effect](common/inline_scripts/jobs/effects/type/tec_brain_drone_effect.txt#L12)
* [jobs/effects/type/tec_bureaucrat_effect](common/inline_scripts/jobs/effects/type/tec_bureaucrat_effect.txt#L11)
* [jobs/effects/type/tec_calculator_effect](common/inline_scripts/jobs/effects/type/tec_calculator_effect.txt#L9)
* [jobs/effects/type/tec_clerk_effect](common/inline_scripts/jobs/effects/type/tec_clerk_effect.txt#L29)
* [jobs/effects/type/tec_coordinator_effect](common/inline_scripts/jobs/effects/type/tec_coordinator_effect.txt#L25)
* [jobs/effects/type/tec_enforcer_effect](common/inline_scripts/jobs/effects/type/tec_enforcer_effect.txt#L34)
* [jobs/effects/type/tec_entertainer_effect](common/inline_scripts/jobs/effects/type/tec_entertainer_effect.txt#L9)
* [jobs/effects/type/tec_farmer_effect](common/inline_scripts/jobs/effects/type/tec_farmer_effect.txt#L19)
* [jobs/effects/type/tec_foundry_drone_effect](common/inline_scripts/jobs/effects/type/tec_foundry_drone_effect.txt#L7)
* [jobs/effects/type/tec_foundry_effect](common/inline_scripts/jobs/effects/type/tec_foundry_effect.txt#L10)
* [jobs/effects/type/tec_livestock_effect](common/inline_scripts/jobs/effects/type/tec_organic_batteries_effect.txt#L29)
* [jobs/effects/type/tec_maintenance_drone_effect](common/inline_scripts/jobs/effects/type/tec_maintenance_drone_effect.txt#L19)
* [jobs/effects/type/tec_manager_effect](common/inline_scripts/jobs/effects/type/tec_manager_effect.txt#L7)
* [jobs/effects/type/tec_miner_effect](common/inline_scripts/jobs/effects/type/tec_miner_effect.txt#L21)
* [jobs/effects/type/tec_mining_drone_effect](common/inline_scripts/jobs/effects/type/tec_mining_drone_effect.txt#L16)
* [jobs/effects/type/tec_naval_operator_drone_effect](common/inline_scripts/jobs/effects/type/tec_naval_operator_drone_effect.txt#L21)
* [jobs/effects/type/tec_naval_operator_effect](common/inline_scripts/jobs/effects/type/tec_naval_operator_effect.txt#L27)
* [jobs/effects/type/tec_patrol_drone_effect](common/inline_scripts/jobs/effects/type/tec_patrol_drone_effect.txt#L19)
* [jobs/effects/type/tec_priest_effect](common/inline_scripts/jobs/effects/type/tec_priest_effect.txt#L9)
* [jobs/effects/type/tec_prime_drone_effect](common/inline_scripts/jobs/effects/type/tec_prime_drone_effect.txt#L106)
* [jobs/effects/type/tec_researcher_effect](common/inline_scripts/jobs/effects/type/tec_researcher_effect.txt#L18)
* [jobs/effects/type/tec_roboticist_effect](common/inline_scripts/jobs/effects/type/tec_roboticist_effect.txt#L23)
* [jobs/effects/type/tec_soldier_effect](common/inline_scripts/jobs/effects/type/tec_soldier_effect.txt#L45)
* [jobs/effects/type/tec_synapse_effect](common/inline_scripts/jobs/effects/type/tec_synapse_effect.txt#L17)
* [jobs/effects/type/tec_technician_drone_effect](common/inline_scripts/jobs/effects/type/tec_technician_drone_effect.txt#L9)
* [jobs/effects/type/tec_technician_effect](common/inline_scripts/jobs/effects/type/tec_technician_effect.txt#L14)
* [jobs/effects/type/tec_trader_effect](common/inline_scripts/jobs/effects/type/tec_trader_effect.txt#L9)
* [jobs/effects/type/tec_warrior_drone_effect](common/inline_scripts/jobs/effects/type/tec_warrior_drone_effect.txt#L23)
* [jobs/tec_clerk](common/inline_scripts/jobs/tec_clerk.txt#L78)
* [jobs/tec_colonist](common/inline_scripts/jobs/tec_colonist.txt#L27)
* [jobs/tec_colonist_colony_swap](common/inline_scripts/jobs/tec_colonist_colony_swap.txt#L51)
* [jobs/tec_coordinator](common/inline_scripts/jobs/tec_coordinator.txt#L32)
* [jobs/tec_enforcer](common/inline_scripts/jobs/tec_enforcer.txt#L28)
* [jobs/tec_entertainer](common/inline_scripts/jobs/tec_entertainer.txt#L49)
* [jobs/tec_executive_civic_swaps](common/inline_scripts/jobs/tec_executive_civic_swaps.txt#L162)
* [jobs/tec_farmer](common/inline_scripts/jobs/_tec_farmer.txt#L164)
* [jobs/tec_farmer_secondary](common/inline_scripts/jobs/tec_farmer_secondary.txt#L67)
* [jobs/tec_foundry](common/inline_scripts/jobs/tec_foundry.txt#L217)
* [jobs/tec_healthcare](common/inline_scripts/jobs/tec_healthcare.txt#L49)
* [jobs/tec_maintenance_civic_hive_swaps](common/inline_scripts/jobs/tec_maintenance_civic_hive_swaps.txt#L25)
* [jobs/tec_maintenance_civic_machine_swaps](common/inline_scripts/jobs/tec_maintenance_civic_machine_swaps.txt#L6)
* [jobs/tec_maintenance_drone](common/inline_scripts/jobs/tec_maintenance_drone.txt#L30)
* [jobs/tec_miner](common/inline_scripts/jobs/_tec_miner.txt#L311)
* [jobs/tec_miner_secondary](common/inline_scripts/jobs/tec_miner_secondary.txt#L69)
* [jobs/tec_patrol_drone](common/inline_scripts/jobs/tec_patrol_drone.txt#L28)
* [jobs/tec_politician_civic_swaps](common/inline_scripts/jobs/tec_politician_civic_swaps.txt#L248)
* [jobs/tec_priest](common/inline_scripts/jobs/tec_priest.txt#L192)
* [jobs/tec_priest_swaps](common/inline_scripts/jobs/tec_priest_swaps.txt#L92)
* [jobs/tec_prime_drone](common/inline_scripts/jobs/tec_prime_drone.txt#L206)
* [jobs/tec_researcher](common/inline_scripts/jobs/tec_researcher.txt#L214)
* [jobs/tec_researcher_swaps](common/inline_scripts/jobs/tec_researcher_swaps.txt#L75)
* [jobs/tec_soldier](common/inline_scripts/jobs/tec_soldier.txt#L118)
* [jobs/tec_spawning_drone](common/inline_scripts/jobs/tec_spawning_drone.txt#L50)
* [jobs/tec_synapse_civic_swaps](common/inline_scripts/jobs/tec_synapse_civic_swaps.txt#L78)
* [jobs/tec_technician](common/inline_scripts/jobs/_tec_technician.txt#L140)
* [jobs/tec_technician_secondary](common/inline_scripts/jobs/tec_technician_secondary.txt#L45)
* [jobs/tec_warrior_drone](common/inline_scripts/jobs/tec_warrior_drone.txt#L29)
* [jobs/weights/tec_clerk](common/inline_scripts/jobs/weights/tec_clerk.txt#L5)
* [jobs/weights/tec_maintenance_drone](common/inline_scripts/jobs/weights/tec_maintenance_drone.txt#L5)
* [mod_support/tec_spiritualist_cults](common/inline_scripts/mod_support/tec_spiritualist_cults.txt#L5)
* [modifiers/tec_artisan_efficiency](common/inline_scripts/modifiers/_tec_artisan_efficiency.txt#L120)
* [modifiers/tec_farmer_efficiency](common/inline_scripts/modifiers/_tec_farmer_efficiency.txt#L42)
* [modifiers/tec_foundry_efficiency](common/inline_scripts/modifiers/_tec_foundry_efficiency.txt#L106)
* [modifiers/tec_miner_efficiency](common/inline_scripts/modifiers/_tec_miner_efficiency.txt#L78)
* [modifiers/tec_rural_farming_district_build_speed](common/inline_scripts/modifiers/tec_rural_farming_district_build_speed.txt#L122)
* [modifiers/tec_rural_farming_district_max](common/inline_scripts/modifiers/tec_rural_farming_district_max.txt#L27)
* [modifiers/tec_rural_generator_district_build_speed](common/inline_scripts/modifiers/tec_rural_generator_district_build_speed.txt#L122)
* [modifiers/tec_rural_generator_district_max](common/inline_scripts/modifiers/tec_rural_generator_district_max.txt#L20)
* [modifiers/tec_rural_mining_district_build_speed](common/inline_scripts/modifiers/tec_rural_mining_district_build_speed.txt#L122)
* [modifiers/tec_rural_mining_district_max](common/inline_scripts/modifiers/tec_rural_mining_district_max.txt#L20)
* [modifiers/tec_technician_efficiency](common/inline_scripts/modifiers/_tec_technician_efficiency.txt#L42)
* [traits/tec_extend_trait_adaptive](common/traits/04_species_traits.txt#L605)
* [traits/tec_extend_trait_adaptive_lithoid](common/traits/09_ascension_traits.txt#L4)
* [traits/tec_extend_trait_advanced_budding](common/traits/09_ascension_traits.txt#L745)
* [traits/tec_extend_trait_advanced_gaseous_byproducts](common/traits/09_ascension_traits.txt#L522)
* [traits/tec_extend_trait_advanced_phototrophic](common/traits/09_ascension_traits.txt#L642)
* [traits/tec_extend_trait_advanced_radiotrophic](common/traits/09_ascension_traits.txt#L689)
* [traits/tec_extend_trait_advanced_scintillating](common/traits/09_ascension_traits.txt#L459)
* [traits/tec_extend_trait_advanced_volatile_excretions](common/traits/09_ascension_traits.txt#L580)
* [traits/tec_extend_trait_agrarian](common/traits/04_species_traits.txt#L95)
* [traits/tec_extend_trait_artificial_intelligence](common/traits/09_tox_traits.txt#L753)
* [traits/tec_extend_trait_auto_mod_biological](common/traits/04_species_traits.txt#L46)
* [traits/tec_extend_trait_auto_mod_cyborg](common/traits/10_species_traits_cyborg.txt#L3)
* [traits/tec_extend_trait_auto_mod_overtuned](common/traits/09_tox_traits.txt#L255)
* [traits/tec_extend_trait_auto_mod_robotic](common/traits/05_species_traits_robotic.txt#L45)
* [traits/tec_extend_trait_bioadaptability](common/traits/04_species_traits.txt#L2392)
* [traits/tec_extend_trait_charismatic](common/traits/04_species_traits.txt#L1463)
* [traits/tec_extend_trait_commercial_genius](common/traits/09_tox_traits.txt#L586)
* [traits/tec_extend_trait_communal](common/traits/04_species_traits.txt#L1380)
* [traits/tec_extend_trait_conformists](common/traits/04_species_traits.txt#L1565)
* [traits/tec_extend_trait_conservational](common/traits/04_species_traits.txt#L1892)
* [traits/tec_extend_trait_crack_miner](common/traits/09_tox_traits.txt#L465)
* [traits/tec_extend_trait_crafted_smiles](common/traits/09_tox_traits.txt#L651)
* [traits/tec_extend_trait_cybernetic](common/traits/04_species_traits.txt#L1990)
* [traits/tec_extend_trait_cyborg_ancient_dreadnought](common/traits/10_species_traits_cyborg.txt#L1183)
* [traits/tec_extend_trait_cyborg_apathy_loops](common/traits/10_species_traits_cyborg.txt#L783)
* [traits/tec_extend_trait_cyborg_bionic_engineers](common/traits/10_species_traits_cyborg.txt#L815)
* [traits/tec_extend_trait_cyborg_bionic_physicists](common/traits/10_species_traits_cyborg.txt#L849)
* [traits/tec_extend_trait_cyborg_bionic_sociologists](common/traits/10_species_traits_cyborg.txt#L883)
* [traits/tec_extend_trait_cyborg_bulky](common/traits/10_species_traits_cyborg.txt#L357)
* [traits/tec_extend_trait_cyborg_climate_adjustment_dry](common/traits/10_species_traits_cyborg.txt#L1048)
* [traits/tec_extend_trait_cyborg_climate_adjustment_frozen](common/traits/10_species_traits_cyborg.txt#L1138)
* [traits/tec_extend_trait_cyborg_climate_adjustment_wet](common/traits/10_species_traits_cyborg.txt#L1093)
* [traits/tec_extend_trait_cyborg_creed_of_construction](common/traits/10_species_traits_cyborg.txt#L1336)
* [traits/tec_extend_trait_cyborg_creed_of_labor](common/traits/10_species_traits_cyborg.txt#L1457)
* [traits/tec_extend_trait_cyborg_creed_of_research](common/traits/10_species_traits_cyborg.txt#L1416)
* [traits/tec_extend_trait_cyborg_creed_of_war](common/traits/10_species_traits_cyborg.txt#L1376)
* [traits/tec_extend_trait_cyborg_delicate_frames](common/traits/10_species_traits_cyborg.txt#L951)
* [traits/tec_extend_trait_cyborg_double_jointed](common/traits/10_species_traits_cyborg.txt#L318)
* [traits/tec_extend_trait_cyborg_durable](common/traits/10_species_traits_cyborg.txt#L436)
* [traits/tec_extend_trait_cyborg_efficient_processors](common/traits/10_species_traits_cyborg.txt#L196)
* [traits/tec_extend_trait_cyborg_enhanced_memory](common/traits/10_species_traits_cyborg.txt#L397)
* [traits/tec_extend_trait_cyborg_enigmatic_fortress](common/traits/10_species_traits_cyborg.txt#L1220)
* [traits/tec_extend_trait_cyborg_harvesters](common/traits/10_species_traits_cyborg.txt#L98)
* [traits/tec_extend_trait_cyborg_high_bandwidth](common/traits/10_species_traits_cyborg.txt#L645)
* [traits/tec_extend_trait_cyborg_high_maintenance](common/traits/10_species_traits_cyborg.txt#L470)
* [traits/tec_extend_trait_cyborg_infinity_sphere](common/traits/10_species_traits_cyborg.txt#L1256)
* [traits/tec_extend_trait_cyborg_integrated_weaponry](common/traits/10_species_traits_cyborg.txt#L917)
* [traits/tec_extend_trait_cyborg_learning_algorithms](common/traits/10_species_traits_cyborg.txt#L506)
* [traits/tec_extend_trait_cyborg_limited_memory](common/traits/10_species_traits_cyborg.txt#L983)
* [traits/tec_extend_trait_cyborg_logic_engines](common/traits/10_species_traits_cyborg.txt#L239)
* [traits/tec_extend_trait_cyborg_loyalty_circuits](common/traits/10_species_traits_cyborg.txt#L280)
* [traits/tec_extend_trait_cyborg_neural_limiters](common/traits/10_species_traits_cyborg.txt#L574)
* [traits/tec_extend_trait_cyborg_power_drills](common/traits/10_species_traits_cyborg.txt#L48)
* [traits/tec_extend_trait_cyborg_power_intensive](common/traits/10_species_traits_cyborg.txt#L544)
* [traits/tec_extend_trait_cyborg_ritualistic_implants](common/traits/10_species_traits_cyborg.txt#L1496)
* [traits/tec_extend_trait_cyborg_scarcity_algorithms](common/traits/10_species_traits_cyborg.txt#L1014)
* [traits/tec_extend_trait_cyborg_scavenger_bot](common/traits/10_species_traits_cyborg.txt#L1292)
* [traits/tec_extend_trait_cyborg_stainless_steel_smile](common/traits/10_species_traits_cyborg.txt#L719)
* [traits/tec_extend_trait_cyborg_streamlined_protocols](common/traits/10_species_traits_cyborg.txt#L614)
* [traits/tec_extend_trait_cyborg_superconductive](common/traits/10_species_traits_cyborg.txt#L148)
* [traits/tec_extend_trait_cyborg_trading_algorithms](common/traits/10_species_traits_cyborg.txt#L675)
* [traits/tec_extend_trait_cyborg_welded_countenance](common/traits/10_species_traits_cyborg.txt#L752)
* [traits/tec_extend_trait_decadent](common/traits/04_species_traits.txt#L1811)
* [traits/tec_extend_trait_delicious](common/traits/09_ascension_traits.txt#L127)
* [traits/tec_extend_trait_deviants](common/traits/04_species_traits.txt#L1612)
* [traits/tec_extend_trait_docile](common/traits/04_species_traits.txt#L1045)
* [traits/tec_extend_trait_drake_scaled](common/traits/09_ascension_traits.txt#L991)
* [traits/tec_extend_trait_elevated_synapses](common/traits/09_tox_traits.txt#L942)
* [traits/tec_extend_trait_enduring](common/traits/04_species_traits.txt#L1695)
* [traits/tec_extend_trait_enigmatic_intelligence](common/traits/04_species_traits.txt#L2244)
* [traits/tec_extend_trait_enigmatic_intelligence_failed](common/traits/04_species_traits.txt#L2344)
* [traits/tec_extend_trait_enigmatic_intelligence_poor](common/traits/04_species_traits.txt#L2297)
* [traits/tec_extend_trait_erudite](common/traits/09_ascension_traits.txt#L382)
* [traits/tec_extend_trait_excessive_endurance](common/traits/09_tox_traits.txt#L1073)
* [traits/tec_extend_trait_exotic_metabolism](common/traits/09_tox_traits.txt#L206)
* [traits/tec_extend_trait_expressed_tradition](common/traits/09_tox_traits.txt#L879)
* [traits/tec_extend_trait_extremely_adaptive](common/traits/04_species_traits.txt#L556)
* [traits/tec_extend_trait_farm_hands](common/traits/09_tox_traits.txt#L403)
* [traits/tec_extend_trait_felsic](common/traits/09_ascension_traits.txt#L900)
* [traits/tec_extend_trait_fertile](common/traits/09_ascension_traits.txt#L263)
* [traits/tec_extend_trait_fleeting](common/traits/04_species_traits.txt#L1737)
* [traits/tec_extend_trait_fleeting_lithoid](common/traits/04_species_traits.txt#L1773)
* [traits/tec_extend_trait_gene_mentorship](common/traits/09_tox_traits.txt#L819)
* [traits/tec_extend_trait_harvested_radiotrophic](common/traits/04_species_traits.txt#L3260)
* [traits/tec_extend_trait_humanoid_existential_iteroparity](common/traits/04_species_traits.txt#L3451)
* [traits/tec_extend_trait_humanoid_jinxed](common/traits/04_species_traits.txt#L3592)
* [traits/tec_extend_trait_humanoid_psychological_infertility](common/traits/04_species_traits.txt#L3531)
* [traits/tec_extend_trait_incubator](common/traits/09_tox_traits.txt#L45)
* [traits/tec_extend_trait_industrious](common/traits/04_species_traits.txt#L188)
* [traits/tec_extend_trait_ingenious](common/traits/04_species_traits.txt#L141)
* [traits/tec_extend_trait_inorganic_breath](common/traits/09_tox_traits.txt#L121)
* [traits/tec_extend_trait_intelligent](common/traits/04_species_traits.txt#L234)
* [traits/tec_extend_trait_invasive](common/traits/04_species_traits.txt#L3071)
* [traits/tec_extend_trait_juiced_power](common/traits/09_tox_traits.txt#L344)
* [traits/tec_extend_trait_latent_psionic](common/traits/04_species_traits.txt#L2060)
* [traits/tec_extend_trait_limited_regeneration](common/traits/04_species_traits.txt#L2457)
* [traits/tec_extend_trait_lithoid_budding](common/traits/04_species_traits.txt#L3187)
* [traits/tec_extend_trait_lithoid_gaseous_byproducts](common/traits/04_species_traits.txt#L2542)
* [traits/tec_extend_trait_lithoid_radiotrophic](common/traits/04_species_traits.txt#L3324)
* [traits/tec_extend_trait_lithoid_scintillating](common/traits/04_species_traits.txt#L2491)
* [traits/tec_extend_trait_lithoid_volatile_excretions](common/traits/04_species_traits.txt#L2592)
* [traits/tec_extend_trait_low_maintenance](common/traits/09_tox_traits.txt#L702)
* [traits/tec_extend_trait_natural_engineers](common/traits/04_species_traits.txt#L360)
* [traits/tec_extend_trait_natural_machinist](common/traits/09_ascension_traits.txt#L938)
* [traits/tec_extend_trait_natural_physicists](common/traits/04_species_traits.txt#L425)
* [traits/tec_extend_trait_natural_sociologists](common/traits/04_species_traits.txt#L489)
* [traits/tec_extend_trait_nerve_stapled](common/traits/09_ascension_traits.txt#L166)
* [traits/tec_extend_trait_nomadic](common/traits/04_species_traits.txt#L1297)
* [traits/tec_extend_trait_nonadaptive](common/traits/04_species_traits.txt#L654)
* [traits/tec_extend_trait_noxious](common/traits/09_tox_traits.txt#L166)
* [traits/tec_extend_trait_plantoid_bloomed](common/traits/04_species_traits.txt#L2809)
* [traits/tec_extend_trait_plantoid_budding](common/traits/04_species_traits.txt#L2996)
* [traits/tec_extend_trait_plantoid_phototrophic](common/traits/04_species_traits.txt#L2901)
* [traits/tec_extend_trait_plantoid_radiotrophic](common/traits/04_species_traits.txt#L2943)
* [traits/tec_extend_trait_preplanned_growth](common/traits/09_tox_traits.txt#L1011)
* [traits/tec_extend_trait_psionic](common/traits/04_species_traits.txt#L2121)
* [traits/tec_extend_trait_quarrelsome](common/traits/04_species_traits.txt#L1006)
* [traits/tec_extend_trait_quick_learners](common/traits/04_species_traits.txt#L875)
* [traits/tec_extend_trait_rapid_breeders](common/traits/04_species_traits.txt#L692)
* [traits/tec_extend_trait_rapid_breeders_lithoid](common/traits/09_ascension_traits.txt#L51)
* [traits/tec_extend_trait_repugnant](common/traits/04_species_traits.txt#L1506)
* [traits/tec_extend_trait_resilient](common/traits/04_species_traits.txt#L1855)
* [traits/tec_extend_trait_robot_ancient_dreadnought](common/traits/05_species_traits_robotic.txt#L1415)
* [traits/tec_extend_trait_robot_artificial_engineers](common/traits/05_species_traits_robotic.txt#L1182)
* [traits/tec_extend_trait_robot_artificial_physicists](common/traits/05_species_traits_robotic.txt#L1220)
* [traits/tec_extend_trait_robot_artificial_sociologists](common/traits/05_species_traits_robotic.txt#L1257)
* [traits/tec_extend_trait_robot_biomimetic_assembly](common/traits/05_species_traits_robotic.txt#L2126)
* [traits/tec_extend_trait_robot_bulky](common/traits/05_species_traits_robotic.txt#L437)
* [traits/tec_extend_trait_robot_ceaseless_symmetric_annihilation_engine](common/traits/05_species_traits_robotic.txt#L2038)
* [traits/tec_extend_trait_robot_custom_made](common/traits/05_species_traits_robotic.txt#L761)
* [traits/tec_extend_trait_robot_decadent](common/traits/05_species_traits_robotic.txt#L1101)
* [traits/tec_extend_trait_robot_delicate_frames](common/traits/05_species_traits_robotic.txt#L1336)
* [traits/tec_extend_trait_robot_deviants](common/traits/05_species_traits_robotic.txt#L1065)
* [traits/tec_extend_trait_robot_digital_1](common/traits/05_species_traits_robotic.txt#L1813)
* [traits/tec_extend_trait_robot_digital_2](common/traits/05_species_traits_robotic.txt#L1844)
* [traits/tec_extend_trait_robot_domestic_protocols](common/traits/05_species_traits_robotic.txt#L361)
* [traits/tec_extend_trait_robot_double_jointed](common/traits/05_species_traits_robotic.txt#L405)
* [traits/tec_extend_trait_robot_durable](common/traits/05_species_traits_robotic.txt#L586)
* [traits/tec_extend_trait_robot_efficient_processors](common/traits/05_species_traits_robotic.txt#L233)
* [traits/tec_extend_trait_robot_emotion_emulators](common/traits/05_species_traits_robotic.txt#L504)
* [traits/tec_extend_trait_robot_enhanced_memory](common/traits/05_species_traits_robotic.txt#L466)
* [traits/tec_extend_trait_robot_enigmatic_fortress](common/traits/05_species_traits_robotic.txt#L1455)
* [traits/tec_extend_trait_robot_exotic_fuel_consumption](common/traits/05_species_traits_robotic.txt#L2254)
* [traits/tec_extend_trait_robot_ferro_viscosity_augmentation](common/traits/05_species_traits_robotic.txt#L2073)
* [traits/tec_extend_trait_robot_harvesters](common/traits/05_species_traits_robotic.txt#L129)
* [traits/tec_extend_trait_robot_high_bandwidth](common/traits/05_species_traits_robotic.txt#L947)
* [traits/tec_extend_trait_robot_high_maintenance](common/traits/05_species_traits_robotic.txt#L617)
* [traits/tec_extend_trait_robot_history_artbot](common/traits/05_species_traits_robotic.txt#L1610)
* [traits/tec_extend_trait_robot_history_chatbot](common/traits/05_species_traits_robotic.txt#L1752)
* [traits/tec_extend_trait_robot_history_explorebot](common/traits/05_species_traits_robotic.txt#L1645)
* [traits/tec_extend_trait_robot_history_researchbot](common/traits/05_species_traits_robotic.txt#L1680)
* [traits/tec_extend_trait_robot_history_warbot](common/traits/05_species_traits_robotic.txt#L1575)
* [traits/tec_extend_trait_robot_immortality](common/traits/05_species_traits_robotic.txt#L2373)
* [traits/tec_extend_trait_robot_infinity_sphere](common/traits/05_species_traits_robotic.txt#L1494)
* [traits/tec_extend_trait_robot_inquisitative_axioms](common/traits/05_species_traits_robotic.txt#L2002)
* [traits/tec_extend_trait_robot_integrated_weaponry](common/traits/05_species_traits_robotic.txt#L1297)
* [traits/tec_extend_trait_robot_learning_algorithms](common/traits/05_species_traits_robotic.txt#L647)
* [traits/tec_extend_trait_robot_logic_engines](common/traits/05_species_traits_robotic.txt#L273)
* [traits/tec_extend_trait_robot_loyalty_circuits](common/traits/05_species_traits_robotic.txt#L321)
* [traits/tec_extend_trait_robot_luxurious](common/traits/05_species_traits_robotic.txt#L831)
* [traits/tec_extend_trait_robot_mass_produced](common/traits/05_species_traits_robotic.txt#L725)
* [traits/tec_extend_trait_robot_matrix_trading](common/traits/05_species_traits_robotic.txt#L2164)
* [traits/tec_extend_trait_robot_monoform](common/traits/05_species_traits_robotic.txt#L1970)
* [traits/tec_extend_trait_robot_mote_powered_tools](common/traits/05_species_traits_robotic.txt#L2217)
* [traits/tec_extend_trait_robot_power_drills](common/traits/05_species_traits_robotic.txt#L89)
* [traits/tec_extend_trait_robot_propaganda_machines](common/traits/05_species_traits_robotic.txt#L867)
* [traits/tec_extend_trait_robot_quarrelsome](common/traits/05_species_traits_robotic.txt#L1016)
* [traits/tec_extend_trait_robot_rare_crystal_exterior](common/traits/05_species_traits_robotic.txt#L2290)
* [traits/tec_extend_trait_robot_recycled](common/traits/05_species_traits_robotic.txt#L794)
* [traits/tec_extend_trait_robot_repurposed_hardware](common/traits/05_species_traits_robotic.txt#L684)
* [traits/tec_extend_trait_robot_scarcity_algorithms](common/traits/05_species_traits_robotic.txt#L1374)
* [traits/tec_extend_trait_robot_scavenger_bot](common/traits/05_species_traits_robotic.txt#L1533)
* [traits/tec_extend_trait_robot_shielded_components](common/traits/05_species_traits_robotic.txt#L1937)
* [traits/tec_extend_trait_robot_streamlined_protocols](common/traits/05_species_traits_robotic.txt#L917)
* [traits/tec_extend_trait_robot_superconductive](common/traits/05_species_traits_robotic.txt#L191)
* [traits/tec_extend_trait_robot_suppressed](common/traits/05_species_traits_robotic.txt#L1898)
* [traits/tec_extend_trait_robot_survivor](common/traits/05_species_traits_robotic.txt#L1787)
* [traits/tec_extend_trait_robot_synthetic_dawn](common/traits/05_species_traits_robotic.txt#L2415)
* [traits/tec_extend_trait_robot_trading_algorithms](common/traits/05_species_traits_robotic.txt#L974)
* [traits/tec_extend_trait_robot_uncanny](common/traits/05_species_traits_robotic.txt#L543)
* [traits/tec_extend_trait_robot_volatile_mote_reactor](common/traits/05_species_traits_robotic.txt#L2337)
* [traits/tec_extend_trait_robot_wasteful](common/traits/05_species_traits_robotic.txt#L1143)
* [traits/tec_extend_trait_robust](common/traits/09_ascension_traits.txt#L329)
* [traits/tec_extend_trait_sedentary](common/traits/04_species_traits.txt#L1341)
* [traits/tec_extend_trait_self_modified](common/traits/04_species_traits.txt#L2183)
* [traits/tec_extend_trait_slow_breeders](common/traits/04_species_traits.txt#L768)
* [traits/tec_extend_trait_slow_learners](common/traits/04_species_traits.txt#L917)
* [traits/tec_extend_trait_social_pheromones](common/traits/04_species_traits.txt#L2425)
* [traits/tec_extend_trait_solitary](common/traits/04_species_traits.txt#L1425)
* [traits/tec_extend_trait_spliced_adaptability](common/traits/09_tox_traits.txt#L294)
* [traits/tec_extend_trait_strong](common/traits/04_species_traits.txt#L1197)
* [traits/tec_extend_trait_survivor](common/traits/04_species_traits.txt#L2216)
* [traits/tec_extend_trait_talented](common/traits/04_species_traits.txt#L832)
* [traits/tec_extend_trait_tec_auto_mod_biological_pregame](common/traits/00_zz_evolved_pregame_only_traits.txt#L3)
* [traits/tec_extend_trait_tec_auto_mod_robotic_pregame](common/traits/00_zz_evolved_pregame_only_traits.txt#L55)
* [traits/tec_extend_trait_tec_bioservant_domestic_servant](common/traits/zz_evolved_organic_traits.txt#L2886)
* [traits/tec_extend_trait_tec_bioservant_livestock](common/traits/zz_evolved_organic_traits.txt#L2939)
* [traits/tec_extend_trait_tec_decaying_decomposition](common/traits/zz_evolved_organic_traits.txt#L2655)
* [traits/tec_extend_trait_tec_efficient](common/traits/zz_evolved_organic_traits.txt#L548)
* [traits/tec_extend_trait_tec_gifted_engineers](common/traits/zz_evolved_organic_traits.txt#L253)
* [traits/tec_extend_trait_tec_gifted_physicists](common/traits/zz_evolved_organic_traits.txt#L130)
* [traits/tec_extend_trait_tec_gifted_sociologists](common/traits/zz_evolved_organic_traits.txt#L190)
* [traits/tec_extend_trait_tec_goods_upkeep_extreme](common/traits/zz_evolved_organic_traits.txt#L1188)
* [traits/tec_extend_trait_tec_goods_upkeep_superefficient](common/traits/zz_evolved_organic_traits.txt#L1235)
* [traits/tec_extend_trait_tec_inefficient](common/traits/zz_evolved_organic_traits.txt#L598)
* [traits/tec_extend_trait_tec_negated_engineers](common/traits/zz_evolved_organic_traits.txt#L433)
* [traits/tec_extend_trait_tec_negated_physicists](common/traits/zz_evolved_organic_traits.txt#L315)
* [traits/tec_extend_trait_tec_negated_sociologists](common/traits/zz_evolved_organic_traits.txt#L374)
* [traits/tec_extend_trait_tec_predatory_consumption](common/traits/zz_evolved_organic_traits.txt#L2618)
* [traits/tec_extend_trait_tec_robot_domestic_protocols_pregame](common/traits/00_zz_evolved_pregame_only_traits.txt#L150)
* [traits/tec_extend_trait_tec_sterile_pregame](common/traits/00_zz_evolved_pregame_only_traits.txt#L107)
* [traits/tec_extend_trait_tec_upkeep_gluttons](common/traits/zz_evolved_organic_traits.txt#L971)
* [traits/tec_extend_trait_tec_upkeep_voracious](common/traits/zz_evolved_organic_traits.txt#L933)
* [traits/tec_extend_trait_tec_zombification](common/traits/zz_evolved_organic_traits.txt#L2692)
* [traits/tec_extend_trait_technical_skill](common/traits/09_tox_traits.txt#L526)
* [traits/tec_extend_trait_thrifty](common/traits/04_species_traits.txt#L302)
* [traits/tec_extend_trait_tiyanki](common/traits/09_ascension_traits.txt#L1102)
* [traits/tec_extend_trait_traditional](common/traits/04_species_traits.txt#L955)
* [traits/tec_extend_trait_unruly](common/traits/04_species_traits.txt#L1092)
* [traits/tec_extend_trait_uplifted](common/traits/04_species_traits.txt#L1537)
* [traits/tec_extend_trait_vat_grown](common/traits/09_ascension_traits.txt#L827)
* [traits/tec_extend_trait_venerable](common/traits/04_species_traits.txt#L1649)
* [traits/tec_extend_trait_very_strong](common/traits/04_species_traits.txt#L1130)
* [traits/tec_extend_trait_void_dweller_1](common/traits/04_species_traits.txt#L2642)
* [traits/tec_extend_trait_void_dweller_2](common/traits/04_species_traits.txt#L2747)
* [traits/tec_extend_trait_voidling](common/traits/09_ascension_traits.txt#L1047)
* [traits/tec_extend_trait_wasteful](common/traits/04_species_traits.txt#L1944)
* [traits/tec_extend_trait_weak](common/traits/04_species_traits.txt#L1259)
* [traits/tec_extend_trait_zombie](common/traits/04_species_traits.txt#L3378)

## Authorities with extendable swaps without overwrites

* [auth_corporate](common/governments/authorities/00_authorities.txt#L874) - use inline evolved_support/governments/authorities/tec_auth_corporate_swaps_\<suffix\>.txt
* [auth_democratic](common/governments/authorities/00_authorities.txt#L78) - use inline evolved_support/governments/authorities/tec_auth_democratic_swaps_\<suffix\>.txt
* [auth_dictatorial](common/governments/authorities/00_authorities.txt#L501) - use inline evolved_support/governments/authorities/tec_auth_dictatorial_swaps_\<suffix\>.txt
* [auth_hive_mind](common/governments/authorities/00_authorities.txt#L1229) - use inline evolved_support/governments/authorities/tec_auth_hive_mind_swaps_\<suffix\>.txt
* [auth_imperial](common/governments/authorities/00_authorities.txt#L729) - use inline evolved_support/governments/authorities/tec_auth_imperial_swaps_\<suffix\>.txt
* [auth_machine_intelligence](common/governments/authorities/00_authorities.txt#L1517) - use inline evolved_support/governments/authorities/tec_auth_machine_intelligence_swaps_\<suffix\>.txt
* [auth_oligarchic](common/governments/authorities/00_authorities.txt#L302) - use inline evolved_support/governments/authorities/tec_auth_oligarchic_swaps_\<suffix\>.txt
* [auth_tec_ai](common/governments/authorities/00_authorities.txt#L1094) - use inline evolved_support/governments/authorities/tec_auth_tec_ai_swaps_\<suffix\>.txt
* [auth_tec_ai_corporate](common/governments/authorities/00_authorities.txt#L1160) - use inline evolved_support/governments/authorities/tec_auth_tec_ai_corporate_swaps_\<suffix\>.txt
* [auth_tec_hive_biological](common/governments/authorities/00_authorities.txt#L1325) - use inline evolved_support/governments/authorities/tec_auth_tec_hive_biological_swaps_\<suffix\>.txt
* [auth_tec_hive_biomechanical](common/governments/authorities/00_authorities.txt#L1451) - use inline evolved_support/governments/authorities/tec_auth_tec_hive_biomechanical_swaps_\<suffix\>.txt
* [auth_tec_hive_cybernetic](common/governments/authorities/00_authorities.txt#L1391) - use inline evolved_support/governments/authorities/tec_auth_tec_hive_cybernetic_swaps_\<suffix\>.txt
* [auth_tec_machine_consensus](common/governments/authorities/00_authorities.txt#L1632) - use inline evolved_support/governments/authorities/tec_auth_tec_machine_consensus_swaps_\<suffix\>.txt
* [auth_tec_patrocorporate](common/governments/authorities/00_authorities.txt#L1019) - use inline evolved_support/governments/authorities/tec_auth_tec_patrocorporate_swaps_\<suffix\>.txt
* [auth_tec_theocracy](common/governments/authorities/00_authorities.txt#L438) - use inline evolved_support/governments/authorities/tec_auth_tec_theocracy_swaps_\<suffix\>.txt

## Traits that can be extended without overwrites

* [trait_adaptive](common/traits/04_species_traits.txt#L605) - use inline evolved_support/traits/tec_extend_trait_adaptive_\<suffix\>.txt
* [trait_adaptive_lithoid](common/traits/09_ascension_traits.txt#L4) - use inline evolved_support/traits/tec_extend_trait_adaptive_lithoid_\<suffix\>.txt
* [trait_advanced_budding](common/traits/09_ascension_traits.txt#L745) - use inline evolved_support/traits/tec_extend_trait_advanced_budding_\<suffix\>.txt
* [trait_advanced_gaseous_byproducts](common/traits/09_ascension_traits.txt#L522) - use inline evolved_support/traits/tec_extend_trait_advanced_gaseous_byproducts_\<suffix\>.txt
* [trait_advanced_phototrophic](common/traits/09_ascension_traits.txt#L642) - use inline evolved_support/traits/tec_extend_trait_advanced_phototrophic_\<suffix\>.txt
* [trait_advanced_radiotrophic](common/traits/09_ascension_traits.txt#L689) - use inline evolved_support/traits/tec_extend_trait_advanced_radiotrophic_\<suffix\>.txt
* [trait_advanced_scintillating](common/traits/09_ascension_traits.txt#L459) - use inline evolved_support/traits/tec_extend_trait_advanced_scintillating_\<suffix\>.txt
* [trait_advanced_volatile_excretions](common/traits/09_ascension_traits.txt#L580) - use inline evolved_support/traits/tec_extend_trait_advanced_volatile_excretions_\<suffix\>.txt
* [trait_agrarian](common/traits/04_species_traits.txt#L95) - use inline evolved_support/traits/tec_extend_trait_agrarian_\<suffix\>.txt
* [trait_artificial_intelligence](common/traits/09_tox_traits.txt#L753) - use inline evolved_support/traits/tec_extend_trait_artificial_intelligence_\<suffix\>.txt
* [trait_auto_mod_biological](common/traits/04_species_traits.txt#L46) - use inline evolved_support/traits/tec_extend_trait_auto_mod_biological_\<suffix\>.txt
* [trait_auto_mod_cyborg](common/traits/10_species_traits_cyborg.txt#L3) - use inline evolved_support/traits/tec_extend_trait_auto_mod_cyborg_\<suffix\>.txt
* [trait_auto_mod_overtuned](common/traits/09_tox_traits.txt#L255) - use inline evolved_support/traits/tec_extend_trait_auto_mod_overtuned_\<suffix\>.txt
* [trait_auto_mod_robotic](common/traits/05_species_traits_robotic.txt#L45) - use inline evolved_support/traits/tec_extend_trait_auto_mod_robotic_\<suffix\>.txt
* [trait_bioadaptability](common/traits/04_species_traits.txt#L2392) - use inline evolved_support/traits/tec_extend_trait_bioadaptability_\<suffix\>.txt
* [trait_charismatic](common/traits/04_species_traits.txt#L1463) - use inline evolved_support/traits/tec_extend_trait_charismatic_\<suffix\>.txt
* [trait_commercial_genius](common/traits/09_tox_traits.txt#L586) - use inline evolved_support/traits/tec_extend_trait_commercial_genius_\<suffix\>.txt
* [trait_communal](common/traits/04_species_traits.txt#L1380) - use inline evolved_support/traits/tec_extend_trait_communal_\<suffix\>.txt
* [trait_conformists](common/traits/04_species_traits.txt#L1565) - use inline evolved_support/traits/tec_extend_trait_conformists_\<suffix\>.txt
* [trait_conservational](common/traits/04_species_traits.txt#L1892) - use inline evolved_support/traits/tec_extend_trait_conservational_\<suffix\>.txt
* [trait_crack_miner](common/traits/09_tox_traits.txt#L465) - use inline evolved_support/traits/tec_extend_trait_crack_miner_\<suffix\>.txt
* [trait_crafted_smiles](common/traits/09_tox_traits.txt#L651) - use inline evolved_support/traits/tec_extend_trait_crafted_smiles_\<suffix\>.txt
* [trait_cybernetic](common/traits/04_species_traits.txt#L1990) - use inline evolved_support/traits/tec_extend_trait_cybernetic_\<suffix\>.txt
* [trait_cyborg_ancient_dreadnought](common/traits/10_species_traits_cyborg.txt#L1183) - use inline evolved_support/traits/tec_extend_trait_cyborg_ancient_dreadnought_\<suffix\>.txt
* [trait_cyborg_apathy_loops](common/traits/10_species_traits_cyborg.txt#L783) - use inline evolved_support/traits/tec_extend_trait_cyborg_apathy_loops_\<suffix\>.txt
* [trait_cyborg_bionic_engineers](common/traits/10_species_traits_cyborg.txt#L815) - use inline evolved_support/traits/tec_extend_trait_cyborg_bionic_engineers_\<suffix\>.txt
* [trait_cyborg_bionic_physicists](common/traits/10_species_traits_cyborg.txt#L849) - use inline evolved_support/traits/tec_extend_trait_cyborg_bionic_physicists_\<suffix\>.txt
* [trait_cyborg_bionic_sociologists](common/traits/10_species_traits_cyborg.txt#L883) - use inline evolved_support/traits/tec_extend_trait_cyborg_bionic_sociologists_\<suffix\>.txt
* [trait_cyborg_bulky](common/traits/10_species_traits_cyborg.txt#L357) - use inline evolved_support/traits/tec_extend_trait_cyborg_bulky_\<suffix\>.txt
* [trait_cyborg_climate_adjustment_dry](common/traits/10_species_traits_cyborg.txt#L1048) - use inline evolved_support/traits/tec_extend_trait_cyborg_climate_adjustment_dry_\<suffix\>.txt
* [trait_cyborg_climate_adjustment_frozen](common/traits/10_species_traits_cyborg.txt#L1138) - use inline evolved_support/traits/tec_extend_trait_cyborg_climate_adjustment_frozen_\<suffix\>.txt
* [trait_cyborg_climate_adjustment_wet](common/traits/10_species_traits_cyborg.txt#L1093) - use inline evolved_support/traits/tec_extend_trait_cyborg_climate_adjustment_wet_\<suffix\>.txt
* [trait_cyborg_creed_of_construction](common/traits/10_species_traits_cyborg.txt#L1336) - use inline evolved_support/traits/tec_extend_trait_cyborg_creed_of_construction_\<suffix\>.txt
* [trait_cyborg_creed_of_labor](common/traits/10_species_traits_cyborg.txt#L1457) - use inline evolved_support/traits/tec_extend_trait_cyborg_creed_of_labor_\<suffix\>.txt
* [trait_cyborg_creed_of_research](common/traits/10_species_traits_cyborg.txt#L1416) - use inline evolved_support/traits/tec_extend_trait_cyborg_creed_of_research_\<suffix\>.txt
* [trait_cyborg_creed_of_war](common/traits/10_species_traits_cyborg.txt#L1376) - use inline evolved_support/traits/tec_extend_trait_cyborg_creed_of_war_\<suffix\>.txt
* [trait_cyborg_delicate_frames](common/traits/10_species_traits_cyborg.txt#L951) - use inline evolved_support/traits/tec_extend_trait_cyborg_delicate_frames_\<suffix\>.txt
* [trait_cyborg_double_jointed](common/traits/10_species_traits_cyborg.txt#L318) - use inline evolved_support/traits/tec_extend_trait_cyborg_double_jointed_\<suffix\>.txt
* [trait_cyborg_durable](common/traits/10_species_traits_cyborg.txt#L436) - use inline evolved_support/traits/tec_extend_trait_cyborg_durable_\<suffix\>.txt
* [trait_cyborg_efficient_processors](common/traits/10_species_traits_cyborg.txt#L196) - use inline evolved_support/traits/tec_extend_trait_cyborg_efficient_processors_\<suffix\>.txt
* [trait_cyborg_enhanced_memory](common/traits/10_species_traits_cyborg.txt#L397) - use inline evolved_support/traits/tec_extend_trait_cyborg_enhanced_memory_\<suffix\>.txt
* [trait_cyborg_enigmatic_fortress](common/traits/10_species_traits_cyborg.txt#L1220) - use inline evolved_support/traits/tec_extend_trait_cyborg_enigmatic_fortress_\<suffix\>.txt
* [trait_cyborg_harvesters](common/traits/10_species_traits_cyborg.txt#L98) - use inline evolved_support/traits/tec_extend_trait_cyborg_harvesters_\<suffix\>.txt
* [trait_cyborg_high_bandwidth](common/traits/10_species_traits_cyborg.txt#L645) - use inline evolved_support/traits/tec_extend_trait_cyborg_high_bandwidth_\<suffix\>.txt
* [trait_cyborg_high_maintenance](common/traits/10_species_traits_cyborg.txt#L470) - use inline evolved_support/traits/tec_extend_trait_cyborg_high_maintenance_\<suffix\>.txt
* [trait_cyborg_infinity_sphere](common/traits/10_species_traits_cyborg.txt#L1256) - use inline evolved_support/traits/tec_extend_trait_cyborg_infinity_sphere_\<suffix\>.txt
* [trait_cyborg_integrated_weaponry](common/traits/10_species_traits_cyborg.txt#L917) - use inline evolved_support/traits/tec_extend_trait_cyborg_integrated_weaponry_\<suffix\>.txt
* [trait_cyborg_learning_algorithms](common/traits/10_species_traits_cyborg.txt#L506) - use inline evolved_support/traits/tec_extend_trait_cyborg_learning_algorithms_\<suffix\>.txt
* [trait_cyborg_limited_memory](common/traits/10_species_traits_cyborg.txt#L983) - use inline evolved_support/traits/tec_extend_trait_cyborg_limited_memory_\<suffix\>.txt
* [trait_cyborg_logic_engines](common/traits/10_species_traits_cyborg.txt#L239) - use inline evolved_support/traits/tec_extend_trait_cyborg_logic_engines_\<suffix\>.txt
* [trait_cyborg_loyalty_circuits](common/traits/10_species_traits_cyborg.txt#L280) - use inline evolved_support/traits/tec_extend_trait_cyborg_loyalty_circuits_\<suffix\>.txt
* [trait_cyborg_neural_limiters](common/traits/10_species_traits_cyborg.txt#L574) - use inline evolved_support/traits/tec_extend_trait_cyborg_neural_limiters_\<suffix\>.txt
* [trait_cyborg_power_drills](common/traits/10_species_traits_cyborg.txt#L48) - use inline evolved_support/traits/tec_extend_trait_cyborg_power_drills_\<suffix\>.txt
* [trait_cyborg_power_intensive](common/traits/10_species_traits_cyborg.txt#L544) - use inline evolved_support/traits/tec_extend_trait_cyborg_power_intensive_\<suffix\>.txt
* [trait_cyborg_ritualistic_implants](common/traits/10_species_traits_cyborg.txt#L1496) - use inline evolved_support/traits/tec_extend_trait_cyborg_ritualistic_implants_\<suffix\>.txt
* [trait_cyborg_scarcity_algorithms](common/traits/10_species_traits_cyborg.txt#L1014) - use inline evolved_support/traits/tec_extend_trait_cyborg_scarcity_algorithms_\<suffix\>.txt
* [trait_cyborg_scavenger_bot](common/traits/10_species_traits_cyborg.txt#L1292) - use inline evolved_support/traits/tec_extend_trait_cyborg_scavenger_bot_\<suffix\>.txt
* [trait_cyborg_stainless_steel_smile](common/traits/10_species_traits_cyborg.txt#L719) - use inline evolved_support/traits/tec_extend_trait_cyborg_stainless_steel_smile_\<suffix\>.txt
* [trait_cyborg_streamlined_protocols](common/traits/10_species_traits_cyborg.txt#L614) - use inline evolved_support/traits/tec_extend_trait_cyborg_streamlined_protocols_\<suffix\>.txt
* [trait_cyborg_superconductive](common/traits/10_species_traits_cyborg.txt#L148) - use inline evolved_support/traits/tec_extend_trait_cyborg_superconductive_\<suffix\>.txt
* [trait_cyborg_trading_algorithms](common/traits/10_species_traits_cyborg.txt#L675) - use inline evolved_support/traits/tec_extend_trait_cyborg_trading_algorithms_\<suffix\>.txt
* [trait_cyborg_welded_countenance](common/traits/10_species_traits_cyborg.txt#L752) - use inline evolved_support/traits/tec_extend_trait_cyborg_welded_countenance_\<suffix\>.txt
* [trait_decadent](common/traits/04_species_traits.txt#L1811) - use inline evolved_support/traits/tec_extend_trait_decadent_\<suffix\>.txt
* [trait_delicious](common/traits/09_ascension_traits.txt#L127) - use inline evolved_support/traits/tec_extend_trait_delicious_\<suffix\>.txt
* [trait_deviants](common/traits/04_species_traits.txt#L1612) - use inline evolved_support/traits/tec_extend_trait_deviants_\<suffix\>.txt
* [trait_docile](common/traits/04_species_traits.txt#L1045) - use inline evolved_support/traits/tec_extend_trait_docile_\<suffix\>.txt
* [trait_drake_scaled](common/traits/09_ascension_traits.txt#L991) - use inline evolved_support/traits/tec_extend_trait_drake_scaled_\<suffix\>.txt
* [trait_elevated_synapses](common/traits/09_tox_traits.txt#L942) - use inline evolved_support/traits/tec_extend_trait_elevated_synapses_\<suffix\>.txt
* [trait_enduring](common/traits/04_species_traits.txt#L1695) - use inline evolved_support/traits/tec_extend_trait_enduring_\<suffix\>.txt
* [trait_enigmatic_intelligence](common/traits/04_species_traits.txt#L2244) - use inline evolved_support/traits/tec_extend_trait_enigmatic_intelligence_\<suffix\>.txt
* [trait_enigmatic_intelligence_failed](common/traits/04_species_traits.txt#L2344) - use inline evolved_support/traits/tec_extend_trait_enigmatic_intelligence_failed_\<suffix\>.txt
* [trait_enigmatic_intelligence_poor](common/traits/04_species_traits.txt#L2297) - use inline evolved_support/traits/tec_extend_trait_enigmatic_intelligence_poor_\<suffix\>.txt
* [trait_erudite](common/traits/09_ascension_traits.txt#L382) - use inline evolved_support/traits/tec_extend_trait_erudite_\<suffix\>.txt
* [trait_excessive_endurance](common/traits/09_tox_traits.txt#L1073) - use inline evolved_support/traits/tec_extend_trait_excessive_endurance_\<suffix\>.txt
* [trait_exotic_metabolism](common/traits/09_tox_traits.txt#L206) - use inline evolved_support/traits/tec_extend_trait_exotic_metabolism_\<suffix\>.txt
* [trait_expressed_tradition](common/traits/09_tox_traits.txt#L879) - use inline evolved_support/traits/tec_extend_trait_expressed_tradition_\<suffix\>.txt
* [trait_extremely_adaptive](common/traits/04_species_traits.txt#L556) - use inline evolved_support/traits/tec_extend_trait_extremely_adaptive_\<suffix\>.txt
* [trait_farm_hands](common/traits/09_tox_traits.txt#L403) - use inline evolved_support/traits/tec_extend_trait_farm_hands_\<suffix\>.txt
* [trait_felsic](common/traits/09_ascension_traits.txt#L900) - use inline evolved_support/traits/tec_extend_trait_felsic_\<suffix\>.txt
* [trait_fertile](common/traits/09_ascension_traits.txt#L263) - use inline evolved_support/traits/tec_extend_trait_fertile_\<suffix\>.txt
* [trait_fleeting](common/traits/04_species_traits.txt#L1737) - use inline evolved_support/traits/tec_extend_trait_fleeting_\<suffix\>.txt
* [trait_fleeting_lithoid](common/traits/04_species_traits.txt#L1773) - use inline evolved_support/traits/tec_extend_trait_fleeting_lithoid_\<suffix\>.txt
* [trait_gene_mentorship](common/traits/09_tox_traits.txt#L819) - use inline evolved_support/traits/tec_extend_trait_gene_mentorship_\<suffix\>.txt
* [trait_harvested_radiotrophic](common/traits/04_species_traits.txt#L3260) - use inline evolved_support/traits/tec_extend_trait_harvested_radiotrophic_\<suffix\>.txt
* [trait_humanoid_existential_iteroparity](common/traits/04_species_traits.txt#L3451) - use inline evolved_support/traits/tec_extend_trait_humanoid_existential_iteroparity_\<suffix\>.txt
* [trait_humanoid_jinxed](common/traits/04_species_traits.txt#L3592) - use inline evolved_support/traits/tec_extend_trait_humanoid_jinxed_\<suffix\>.txt
* [trait_humanoid_psychological_infertility](common/traits/04_species_traits.txt#L3531) - use inline evolved_support/traits/tec_extend_trait_humanoid_psychological_infertility_\<suffix\>.txt
* [trait_incubator](common/traits/09_tox_traits.txt#L45) - use inline evolved_support/traits/tec_extend_trait_incubator_\<suffix\>.txt
* [trait_industrious](common/traits/04_species_traits.txt#L188) - use inline evolved_support/traits/tec_extend_trait_industrious_\<suffix\>.txt
* [trait_ingenious](common/traits/04_species_traits.txt#L141) - use inline evolved_support/traits/tec_extend_trait_ingenious_\<suffix\>.txt
* [trait_inorganic_breath](common/traits/09_tox_traits.txt#L121) - use inline evolved_support/traits/tec_extend_trait_inorganic_breath_\<suffix\>.txt
* [trait_intelligent](common/traits/04_species_traits.txt#L234) - use inline evolved_support/traits/tec_extend_trait_intelligent_\<suffix\>.txt
* [trait_invasive](common/traits/04_species_traits.txt#L3071) - use inline evolved_support/traits/tec_extend_trait_invasive_\<suffix\>.txt
* [trait_juiced_power](common/traits/09_tox_traits.txt#L344) - use inline evolved_support/traits/tec_extend_trait_juiced_power_\<suffix\>.txt
* [trait_latent_psionic](common/traits/04_species_traits.txt#L2060) - use inline evolved_support/traits/tec_extend_trait_latent_psionic_\<suffix\>.txt
* [trait_limited_regeneration](common/traits/04_species_traits.txt#L2457) - use inline evolved_support/traits/tec_extend_trait_limited_regeneration_\<suffix\>.txt
* [trait_lithoid_budding](common/traits/04_species_traits.txt#L3187) - use inline evolved_support/traits/tec_extend_trait_lithoid_budding_\<suffix\>.txt
* [trait_lithoid_gaseous_byproducts](common/traits/04_species_traits.txt#L2542) - use inline evolved_support/traits/tec_extend_trait_lithoid_gaseous_byproducts_\<suffix\>.txt
* [trait_lithoid_radiotrophic](common/traits/04_species_traits.txt#L3324) - use inline evolved_support/traits/tec_extend_trait_lithoid_radiotrophic_\<suffix\>.txt
* [trait_lithoid_scintillating](common/traits/04_species_traits.txt#L2491) - use inline evolved_support/traits/tec_extend_trait_lithoid_scintillating_\<suffix\>.txt
* [trait_lithoid_volatile_excretions](common/traits/04_species_traits.txt#L2592) - use inline evolved_support/traits/tec_extend_trait_lithoid_volatile_excretions_\<suffix\>.txt
* [trait_low_maintenance](common/traits/09_tox_traits.txt#L702) - use inline evolved_support/traits/tec_extend_trait_low_maintenance_\<suffix\>.txt
* [trait_natural_engineers](common/traits/04_species_traits.txt#L360) - use inline evolved_support/traits/tec_extend_trait_natural_engineers_\<suffix\>.txt
* [trait_natural_machinist](common/traits/09_ascension_traits.txt#L938) - use inline evolved_support/traits/tec_extend_trait_natural_machinist_\<suffix\>.txt
* [trait_natural_physicists](common/traits/04_species_traits.txt#L425) - use inline evolved_support/traits/tec_extend_trait_natural_physicists_\<suffix\>.txt
* [trait_natural_sociologists](common/traits/04_species_traits.txt#L489) - use inline evolved_support/traits/tec_extend_trait_natural_sociologists_\<suffix\>.txt
* [trait_nerve_stapled](common/traits/09_ascension_traits.txt#L166) - use inline evolved_support/traits/tec_extend_trait_nerve_stapled_\<suffix\>.txt
* [trait_nomadic](common/traits/04_species_traits.txt#L1297) - use inline evolved_support/traits/tec_extend_trait_nomadic_\<suffix\>.txt
* [trait_nonadaptive](common/traits/04_species_traits.txt#L654) - use inline evolved_support/traits/tec_extend_trait_nonadaptive_\<suffix\>.txt
* [trait_noxious](common/traits/09_tox_traits.txt#L166) - use inline evolved_support/traits/tec_extend_trait_noxious_\<suffix\>.txt
* [trait_plantoid_bloomed](common/traits/04_species_traits.txt#L2809) - use inline evolved_support/traits/tec_extend_trait_plantoid_bloomed_\<suffix\>.txt
* [trait_plantoid_budding](common/traits/04_species_traits.txt#L2996) - use inline evolved_support/traits/tec_extend_trait_plantoid_budding_\<suffix\>.txt
* [trait_plantoid_phototrophic](common/traits/04_species_traits.txt#L2901) - use inline evolved_support/traits/tec_extend_trait_plantoid_phototrophic_\<suffix\>.txt
* [trait_plantoid_radiotrophic](common/traits/04_species_traits.txt#L2943) - use inline evolved_support/traits/tec_extend_trait_plantoid_radiotrophic_\<suffix\>.txt
* [trait_preplanned_growth](common/traits/09_tox_traits.txt#L1011) - use inline evolved_support/traits/tec_extend_trait_preplanned_growth_\<suffix\>.txt
* [trait_psionic](common/traits/04_species_traits.txt#L2121) - use inline evolved_support/traits/tec_extend_trait_psionic_\<suffix\>.txt
* [trait_quarrelsome](common/traits/04_species_traits.txt#L1006) - use inline evolved_support/traits/tec_extend_trait_quarrelsome_\<suffix\>.txt
* [trait_quick_learners](common/traits/04_species_traits.txt#L875) - use inline evolved_support/traits/tec_extend_trait_quick_learners_\<suffix\>.txt
* [trait_rapid_breeders](common/traits/04_species_traits.txt#L692) - use inline evolved_support/traits/tec_extend_trait_rapid_breeders_\<suffix\>.txt
* [trait_rapid_breeders_lithoid](common/traits/09_ascension_traits.txt#L51) - use inline evolved_support/traits/tec_extend_trait_rapid_breeders_lithoid_\<suffix\>.txt
* [trait_repugnant](common/traits/04_species_traits.txt#L1506) - use inline evolved_support/traits/tec_extend_trait_repugnant_\<suffix\>.txt
* [trait_resilient](common/traits/04_species_traits.txt#L1855) - use inline evolved_support/traits/tec_extend_trait_resilient_\<suffix\>.txt
* [trait_robot_ancient_dreadnought](common/traits/05_species_traits_robotic.txt#L1415) - use inline evolved_support/traits/tec_extend_trait_robot_ancient_dreadnought_\<suffix\>.txt
* [trait_robot_artificial_engineers](common/traits/05_species_traits_robotic.txt#L1182) - use inline evolved_support/traits/tec_extend_trait_robot_artificial_engineers_\<suffix\>.txt
* [trait_robot_artificial_physicists](common/traits/05_species_traits_robotic.txt#L1220) - use inline evolved_support/traits/tec_extend_trait_robot_artificial_physicists_\<suffix\>.txt
* [trait_robot_artificial_sociologists](common/traits/05_species_traits_robotic.txt#L1257) - use inline evolved_support/traits/tec_extend_trait_robot_artificial_sociologists_\<suffix\>.txt
* [trait_robot_biomimetic_assembly](common/traits/05_species_traits_robotic.txt#L2126) - use inline evolved_support/traits/tec_extend_trait_robot_biomimetic_assembly_\<suffix\>.txt
* [trait_robot_bulky](common/traits/05_species_traits_robotic.txt#L437) - use inline evolved_support/traits/tec_extend_trait_robot_bulky_\<suffix\>.txt
* [trait_robot_ceaseless_symmetric_annihilation_engine](common/traits/05_species_traits_robotic.txt#L2038) - use inline evolved_support/traits/tec_extend_trait_robot_ceaseless_symmetric_annihilation_engine_\<suffix\>.txt
* [trait_robot_custom_made](common/traits/05_species_traits_robotic.txt#L761) - use inline evolved_support/traits/tec_extend_trait_robot_custom_made_\<suffix\>.txt
* [trait_robot_decadent](common/traits/05_species_traits_robotic.txt#L1101) - use inline evolved_support/traits/tec_extend_trait_robot_decadent_\<suffix\>.txt
* [trait_robot_delicate_frames](common/traits/05_species_traits_robotic.txt#L1336) - use inline evolved_support/traits/tec_extend_trait_robot_delicate_frames_\<suffix\>.txt
* [trait_robot_deviants](common/traits/05_species_traits_robotic.txt#L1065) - use inline evolved_support/traits/tec_extend_trait_robot_deviants_\<suffix\>.txt
* [trait_robot_digital_1](common/traits/05_species_traits_robotic.txt#L1813) - use inline evolved_support/traits/tec_extend_trait_robot_digital_1_\<suffix\>.txt
* [trait_robot_digital_2](common/traits/05_species_traits_robotic.txt#L1844) - use inline evolved_support/traits/tec_extend_trait_robot_digital_2_\<suffix\>.txt
* [trait_robot_domestic_protocols](common/traits/05_species_traits_robotic.txt#L361) - use inline evolved_support/traits/tec_extend_trait_robot_domestic_protocols_\<suffix\>.txt
* [trait_robot_double_jointed](common/traits/05_species_traits_robotic.txt#L405) - use inline evolved_support/traits/tec_extend_trait_robot_double_jointed_\<suffix\>.txt
* [trait_robot_durable](common/traits/05_species_traits_robotic.txt#L586) - use inline evolved_support/traits/tec_extend_trait_robot_durable_\<suffix\>.txt
* [trait_robot_efficient_processors](common/traits/05_species_traits_robotic.txt#L233) - use inline evolved_support/traits/tec_extend_trait_robot_efficient_processors_\<suffix\>.txt
* [trait_robot_emotion_emulators](common/traits/05_species_traits_robotic.txt#L504) - use inline evolved_support/traits/tec_extend_trait_robot_emotion_emulators_\<suffix\>.txt
* [trait_robot_enhanced_memory](common/traits/05_species_traits_robotic.txt#L466) - use inline evolved_support/traits/tec_extend_trait_robot_enhanced_memory_\<suffix\>.txt
* [trait_robot_enigmatic_fortress](common/traits/05_species_traits_robotic.txt#L1455) - use inline evolved_support/traits/tec_extend_trait_robot_enigmatic_fortress_\<suffix\>.txt
* [trait_robot_exotic_fuel_consumption](common/traits/05_species_traits_robotic.txt#L2254) - use inline evolved_support/traits/tec_extend_trait_robot_exotic_fuel_consumption_\<suffix\>.txt
* [trait_robot_ferro_viscosity_augmentation](common/traits/05_species_traits_robotic.txt#L2073) - use inline evolved_support/traits/tec_extend_trait_robot_ferro_viscosity_augmentation_\<suffix\>.txt
* [trait_robot_harvesters](common/traits/05_species_traits_robotic.txt#L129) - use inline evolved_support/traits/tec_extend_trait_robot_harvesters_\<suffix\>.txt
* [trait_robot_high_bandwidth](common/traits/05_species_traits_robotic.txt#L947) - use inline evolved_support/traits/tec_extend_trait_robot_high_bandwidth_\<suffix\>.txt
* [trait_robot_high_maintenance](common/traits/05_species_traits_robotic.txt#L617) - use inline evolved_support/traits/tec_extend_trait_robot_high_maintenance_\<suffix\>.txt
* [trait_robot_history_artbot](common/traits/05_species_traits_robotic.txt#L1610) - use inline evolved_support/traits/tec_extend_trait_robot_history_artbot_\<suffix\>.txt
* [trait_robot_history_chatbot](common/traits/05_species_traits_robotic.txt#L1752) - use inline evolved_support/traits/tec_extend_trait_robot_history_chatbot_\<suffix\>.txt
* [trait_robot_history_explorebot](common/traits/05_species_traits_robotic.txt#L1645) - use inline evolved_support/traits/tec_extend_trait_robot_history_explorebot_\<suffix\>.txt
* [trait_robot_history_researchbot](common/traits/05_species_traits_robotic.txt#L1680) - use inline evolved_support/traits/tec_extend_trait_robot_history_researchbot_\<suffix\>.txt
* [trait_robot_history_warbot](common/traits/05_species_traits_robotic.txt#L1575) - use inline evolved_support/traits/tec_extend_trait_robot_history_warbot_\<suffix\>.txt
* [trait_robot_immortality](common/traits/05_species_traits_robotic.txt#L2373) - use inline evolved_support/traits/tec_extend_trait_robot_immortality_\<suffix\>.txt
* [trait_robot_infinity_sphere](common/traits/05_species_traits_robotic.txt#L1494) - use inline evolved_support/traits/tec_extend_trait_robot_infinity_sphere_\<suffix\>.txt
* [trait_robot_inquisitative_axioms](common/traits/05_species_traits_robotic.txt#L2002) - use inline evolved_support/traits/tec_extend_trait_robot_inquisitative_axioms_\<suffix\>.txt
* [trait_robot_integrated_weaponry](common/traits/05_species_traits_robotic.txt#L1297) - use inline evolved_support/traits/tec_extend_trait_robot_integrated_weaponry_\<suffix\>.txt
* [trait_robot_learning_algorithms](common/traits/05_species_traits_robotic.txt#L647) - use inline evolved_support/traits/tec_extend_trait_robot_learning_algorithms_\<suffix\>.txt
* [trait_robot_logic_engines](common/traits/05_species_traits_robotic.txt#L273) - use inline evolved_support/traits/tec_extend_trait_robot_logic_engines_\<suffix\>.txt
* [trait_robot_loyalty_circuits](common/traits/05_species_traits_robotic.txt#L321) - use inline evolved_support/traits/tec_extend_trait_robot_loyalty_circuits_\<suffix\>.txt
* [trait_robot_luxurious](common/traits/05_species_traits_robotic.txt#L831) - use inline evolved_support/traits/tec_extend_trait_robot_luxurious_\<suffix\>.txt
* [trait_robot_mass_produced](common/traits/05_species_traits_robotic.txt#L725) - use inline evolved_support/traits/tec_extend_trait_robot_mass_produced_\<suffix\>.txt
* [trait_robot_matrix_trading](common/traits/05_species_traits_robotic.txt#L2164) - use inline evolved_support/traits/tec_extend_trait_robot_matrix_trading_\<suffix\>.txt
* [trait_robot_monoform](common/traits/05_species_traits_robotic.txt#L1970) - use inline evolved_support/traits/tec_extend_trait_robot_monoform_\<suffix\>.txt
* [trait_robot_mote_powered_tools](common/traits/05_species_traits_robotic.txt#L2217) - use inline evolved_support/traits/tec_extend_trait_robot_mote_powered_tools_\<suffix\>.txt
* [trait_robot_power_drills](common/traits/05_species_traits_robotic.txt#L89) - use inline evolved_support/traits/tec_extend_trait_robot_power_drills_\<suffix\>.txt
* [trait_robot_propaganda_machines](common/traits/05_species_traits_robotic.txt#L867) - use inline evolved_support/traits/tec_extend_trait_robot_propaganda_machines_\<suffix\>.txt
* [trait_robot_quarrelsome](common/traits/05_species_traits_robotic.txt#L1016) - use inline evolved_support/traits/tec_extend_trait_robot_quarrelsome_\<suffix\>.txt
* [trait_robot_rare_crystal_exterior](common/traits/05_species_traits_robotic.txt#L2290) - use inline evolved_support/traits/tec_extend_trait_robot_rare_crystal_exterior_\<suffix\>.txt
* [trait_robot_recycled](common/traits/05_species_traits_robotic.txt#L794) - use inline evolved_support/traits/tec_extend_trait_robot_recycled_\<suffix\>.txt
* [trait_robot_repurposed_hardware](common/traits/05_species_traits_robotic.txt#L684) - use inline evolved_support/traits/tec_extend_trait_robot_repurposed_hardware_\<suffix\>.txt
* [trait_robot_scarcity_algorithms](common/traits/05_species_traits_robotic.txt#L1374) - use inline evolved_support/traits/tec_extend_trait_robot_scarcity_algorithms_\<suffix\>.txt
* [trait_robot_scavenger_bot](common/traits/05_species_traits_robotic.txt#L1533) - use inline evolved_support/traits/tec_extend_trait_robot_scavenger_bot_\<suffix\>.txt
* [trait_robot_shielded_components](common/traits/05_species_traits_robotic.txt#L1937) - use inline evolved_support/traits/tec_extend_trait_robot_shielded_components_\<suffix\>.txt
* [trait_robot_streamlined_protocols](common/traits/05_species_traits_robotic.txt#L917) - use inline evolved_support/traits/tec_extend_trait_robot_streamlined_protocols_\<suffix\>.txt
* [trait_robot_superconductive](common/traits/05_species_traits_robotic.txt#L191) - use inline evolved_support/traits/tec_extend_trait_robot_superconductive_\<suffix\>.txt
* [trait_robot_suppressed](common/traits/05_species_traits_robotic.txt#L1898) - use inline evolved_support/traits/tec_extend_trait_robot_suppressed_\<suffix\>.txt
* [trait_robot_survivor](common/traits/05_species_traits_robotic.txt#L1787) - use inline evolved_support/traits/tec_extend_trait_robot_survivor_\<suffix\>.txt
* [trait_robot_synthetic_dawn](common/traits/05_species_traits_robotic.txt#L2415) - use inline evolved_support/traits/tec_extend_trait_robot_synthetic_dawn_\<suffix\>.txt
* [trait_robot_trading_algorithms](common/traits/05_species_traits_robotic.txt#L974) - use inline evolved_support/traits/tec_extend_trait_robot_trading_algorithms_\<suffix\>.txt
* [trait_robot_uncanny](common/traits/05_species_traits_robotic.txt#L543) - use inline evolved_support/traits/tec_extend_trait_robot_uncanny_\<suffix\>.txt
* [trait_robot_volatile_mote_reactor](common/traits/05_species_traits_robotic.txt#L2337) - use inline evolved_support/traits/tec_extend_trait_robot_volatile_mote_reactor_\<suffix\>.txt
* [trait_robot_wasteful](common/traits/05_species_traits_robotic.txt#L1143) - use inline evolved_support/traits/tec_extend_trait_robot_wasteful_\<suffix\>.txt
* [trait_robust](common/traits/09_ascension_traits.txt#L329) - use inline evolved_support/traits/tec_extend_trait_robust_\<suffix\>.txt
* [trait_sedentary](common/traits/04_species_traits.txt#L1341) - use inline evolved_support/traits/tec_extend_trait_sedentary_\<suffix\>.txt
* [trait_self_modified](common/traits/04_species_traits.txt#L2183) - use inline evolved_support/traits/tec_extend_trait_self_modified_\<suffix\>.txt
* [trait_slow_breeders](common/traits/04_species_traits.txt#L768) - use inline evolved_support/traits/tec_extend_trait_slow_breeders_\<suffix\>.txt
* [trait_slow_learners](common/traits/04_species_traits.txt#L917) - use inline evolved_support/traits/tec_extend_trait_slow_learners_\<suffix\>.txt
* [trait_social_pheromones](common/traits/04_species_traits.txt#L2425) - use inline evolved_support/traits/tec_extend_trait_social_pheromones_\<suffix\>.txt
* [trait_solitary](common/traits/04_species_traits.txt#L1425) - use inline evolved_support/traits/tec_extend_trait_solitary_\<suffix\>.txt
* [trait_spliced_adaptability](common/traits/09_tox_traits.txt#L294) - use inline evolved_support/traits/tec_extend_trait_spliced_adaptability_\<suffix\>.txt
* [trait_strong](common/traits/04_species_traits.txt#L1197) - use inline evolved_support/traits/tec_extend_trait_strong_\<suffix\>.txt
* [trait_survivor](common/traits/04_species_traits.txt#L2216) - use inline evolved_support/traits/tec_extend_trait_survivor_\<suffix\>.txt
* [trait_talented](common/traits/04_species_traits.txt#L832) - use inline evolved_support/traits/tec_extend_trait_talented_\<suffix\>.txt
* [trait_tec_auto_mod_biological_pregame](common/traits/00_zz_evolved_pregame_only_traits.txt#L3) - use inline evolved_support/traits/tec_extend_trait_tec_auto_mod_biological_pregame_\<suffix\>.txt
* [trait_tec_auto_mod_robotic_pregame](common/traits/00_zz_evolved_pregame_only_traits.txt#L55) - use inline evolved_support/traits/tec_extend_trait_tec_auto_mod_robotic_pregame_\<suffix\>.txt
* [trait_tec_bioservant_domestic_servant](common/traits/zz_evolved_organic_traits.txt#L2886) - use inline evolved_support/traits/tec_extend_trait_tec_bioservant_domestic_servant_\<suffix\>.txt
* [trait_tec_bioservant_livestock](common/traits/zz_evolved_organic_traits.txt#L2939) - use inline evolved_support/traits/tec_extend_trait_tec_bioservant_livestock_\<suffix\>.txt
* [trait_tec_decaying_decomposition](common/traits/zz_evolved_organic_traits.txt#L2655) - use inline evolved_support/traits/tec_extend_trait_tec_decaying_decomposition_\<suffix\>.txt
* [trait_tec_efficient](common/traits/zz_evolved_organic_traits.txt#L548) - use inline evolved_support/traits/tec_extend_trait_tec_efficient_\<suffix\>.txt
* [trait_tec_gifted_engineers](common/traits/zz_evolved_organic_traits.txt#L253) - use inline evolved_support/traits/tec_extend_trait_tec_gifted_engineers_\<suffix\>.txt
* [trait_tec_gifted_physicists](common/traits/zz_evolved_organic_traits.txt#L130) - use inline evolved_support/traits/tec_extend_trait_tec_gifted_physicists_\<suffix\>.txt
* [trait_tec_gifted_sociologists](common/traits/zz_evolved_organic_traits.txt#L190) - use inline evolved_support/traits/tec_extend_trait_tec_gifted_sociologists_\<suffix\>.txt
* [trait_tec_goods_upkeep_extreme](common/traits/zz_evolved_organic_traits.txt#L1188) - use inline evolved_support/traits/tec_extend_trait_tec_goods_upkeep_extreme_\<suffix\>.txt
* [trait_tec_goods_upkeep_superefficient](common/traits/zz_evolved_organic_traits.txt#L1235) - use inline evolved_support/traits/tec_extend_trait_tec_goods_upkeep_superefficient_\<suffix\>.txt
* [trait_tec_inefficient](common/traits/zz_evolved_organic_traits.txt#L598) - use inline evolved_support/traits/tec_extend_trait_tec_inefficient_\<suffix\>.txt
* [trait_tec_negated_engineers](common/traits/zz_evolved_organic_traits.txt#L433) - use inline evolved_support/traits/tec_extend_trait_tec_negated_engineers_\<suffix\>.txt
* [trait_tec_negated_physicists](common/traits/zz_evolved_organic_traits.txt#L315) - use inline evolved_support/traits/tec_extend_trait_tec_negated_physicists_\<suffix\>.txt
* [trait_tec_negated_sociologists](common/traits/zz_evolved_organic_traits.txt#L374) - use inline evolved_support/traits/tec_extend_trait_tec_negated_sociologists_\<suffix\>.txt
* [trait_tec_predatory_consumption](common/traits/zz_evolved_organic_traits.txt#L2618) - use inline evolved_support/traits/tec_extend_trait_tec_predatory_consumption_\<suffix\>.txt
* [trait_tec_robot_domestic_protocols_pregame](common/traits/00_zz_evolved_pregame_only_traits.txt#L150) - use inline evolved_support/traits/tec_extend_trait_tec_robot_domestic_protocols_pregame_\<suffix\>.txt
* [trait_tec_sterile_pregame](common/traits/00_zz_evolved_pregame_only_traits.txt#L107) - use inline evolved_support/traits/tec_extend_trait_tec_sterile_pregame_\<suffix\>.txt
* [trait_tec_upkeep_gluttons](common/traits/zz_evolved_organic_traits.txt#L971) - use inline evolved_support/traits/tec_extend_trait_tec_upkeep_gluttons_\<suffix\>.txt
* [trait_tec_upkeep_voracious](common/traits/zz_evolved_organic_traits.txt#L933) - use inline evolved_support/traits/tec_extend_trait_tec_upkeep_voracious_\<suffix\>.txt
* [trait_tec_zombification](common/traits/zz_evolved_organic_traits.txt#L2692) - use inline evolved_support/traits/tec_extend_trait_tec_zombification_\<suffix\>.txt
* [trait_technical_skill](common/traits/09_tox_traits.txt#L526) - use inline evolved_support/traits/tec_extend_trait_technical_skill_\<suffix\>.txt
* [trait_thrifty](common/traits/04_species_traits.txt#L302) - use inline evolved_support/traits/tec_extend_trait_thrifty_\<suffix\>.txt
* [trait_tiyanki](common/traits/09_ascension_traits.txt#L1102) - use inline evolved_support/traits/tec_extend_trait_tiyanki_\<suffix\>.txt
* [trait_traditional](common/traits/04_species_traits.txt#L955) - use inline evolved_support/traits/tec_extend_trait_traditional_\<suffix\>.txt
* [trait_unruly](common/traits/04_species_traits.txt#L1092) - use inline evolved_support/traits/tec_extend_trait_unruly_\<suffix\>.txt
* [trait_uplifted](common/traits/04_species_traits.txt#L1537) - use inline evolved_support/traits/tec_extend_trait_uplifted_\<suffix\>.txt
* [trait_vat_grown](common/traits/09_ascension_traits.txt#L827) - use inline evolved_support/traits/tec_extend_trait_vat_grown_\<suffix\>.txt
* [trait_venerable](common/traits/04_species_traits.txt#L1649) - use inline evolved_support/traits/tec_extend_trait_venerable_\<suffix\>.txt
* [trait_very_strong](common/traits/04_species_traits.txt#L1130) - use inline evolved_support/traits/tec_extend_trait_very_strong_\<suffix\>.txt
* [trait_void_dweller_1](common/traits/04_species_traits.txt#L2642) - use inline evolved_support/traits/tec_extend_trait_void_dweller_1_\<suffix\>.txt
* [trait_void_dweller_2](common/traits/04_species_traits.txt#L2747) - use inline evolved_support/traits/tec_extend_trait_void_dweller_2_\<suffix\>.txt
* [trait_voidling](common/traits/09_ascension_traits.txt#L1047) - use inline evolved_support/traits/tec_extend_trait_voidling_\<suffix\>.txt
* [trait_wasteful](common/traits/04_species_traits.txt#L1944) - use inline evolved_support/traits/tec_extend_trait_wasteful_\<suffix\>.txt
* [trait_weak](common/traits/04_species_traits.txt#L1259) - use inline evolved_support/traits/tec_extend_trait_weak_\<suffix\>.txt
* [trait_zombie](common/traits/04_species_traits.txt#L3378) - use inline evolved_support/traits/tec_extend_trait_zombie_\<suffix\>.txt
