# Evolved Moddability and Extension

Stellaris Evolved supports internally a way of extending existing inlines and triggers 
without needing to overwrite Evolved defined files.

## How to identify what can be extended

### Scripted triggers

Scripted triggers that have the `tec_trigger_mod_support` inside their logic,
usually inside an `OR` statement can be extended by creating a scripted trigger
of your own with a suffix appended to the trigger name.

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

Inline scripts that have `mod_support/inline_evolved_inlines_include` inside their logic
allow themselves to be extended by creating an inline inside the `common/inline_scripts/evolved_support`
with the path of the inline you want to extend.

For example if we want to extend as above the main cult swaps of priests,
you will want to extend the `jobs/inline_evolved_priest` inline, which you can do by making
a file at the path `common/inline_scripts/evolved_support/jobs/inline_evolved_priest_<suffix>`, the `<suffix>`
being a specific identifier that we can create and add to evolved for your patch/mod/addon etc.

All parameters of the extended inline will be available in your inline too.

IE, something like below, if your `<suffix>` is `sam`:

```
# file: common/inline_scripts/evolved_support/jobs/inline_evolved_priest_sam.txt

inline_script = {	
    script = jobs/inline_evolved_job
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

## Current supported scripted_triggers

* tec_has_entertainer_swap
* tec_has_enforcer_swap
* tec_has_colonist_swap
* tec_has_clerk_swap
* tec_has_coordinator_swap
* tec_has_soldier_swap
* tec_has_maintenance_swap
* tec_has_patrol_drone_swap
* tec_has_warrior_drone_swap
* tec_has_healthcare_swap
* tec_has_clinic_building_swap
* tec_has_cyborg_clinic_exception
* tec_has_farmer_swap
* tec_has_farmer_planet_swap
* tec_has_miner_swap
* tec_has_miner_planet_swap
* tec_has_scrap_miner
* tec_has_matter_miner
* tec_has_technician_swap
* tec_has_technician_planet_swap
* tec_has_bureaucratic_buildings_swap
* tec_has_monument_buildings_swap
* tec_has_research_lab_buildings_swap
* tec_has_stronghold_buildings_swap
* tec_has_naval_academy_buildings_swap
* tec_is_special_researcher_empire
* tec_replaces_half_researcher_empire
* tec_is_spiritualist_main_cult
* tec_is_spiritualist_secondary_cult
* tec_has_special_ruler_feature
* tec_has_ruler_civic_regular
* tec_has_ruler_civic_mega
* tec_has_ruler_civic_hive
* tec_has_maintenance_drone_swap_civic_hive
* tec_has_ruler_civic_machine
* tec_has_directive_civic_machine
* tec_has_maintenance_drone_swap_civic_machine
* tec_has_forced_living_standard_civic
* tec_has_slaver_civic
* tec_has_spy_civic
* tec_has_diplomatic_civic

## Current supported inline_scripts

* capitals/inline_evolved_common_modifiers
* capitals/inline_evolved_colony_habitat
* capitals/inline_evolved_regular_capital
* capitals/inline_evolved_machine_capital
* capitals/inline_evolved_common_habitat_modifiers
* capitals/inline_evolved_colony
* capitals/inline_evolved_special_capital
* capitals/inline_evolved_all_capital
* capitals/inline_evolved_hive_capital
* districts/type/inline_evolved_housing_nexus
* districts/type/inline_evolved_housing_habitat
* districts/type/inline_evolved_rural_mining
* districts/type/inline_evolved_housing_hive
* districts/type/inline_evolved_housing_generic
* districts/type/inline_evolved_housing_city
* districts/type/inline_evolved_housing_arcology
* districts/type/inline_evolved_trade
* districts/type/inline_evolved_rural_generator
* districts/type/inline_evolved_rural_farming
* jobs/inline_evolved_technician
* jobs/inline_evolved_priest
* jobs/capital/inline_evolved_add_ruler_civic_regular
* jobs/capital/inline_evolved_add_job_civic_hive
* jobs/capital/inline_evolved_add_job_civic_regular
* jobs/capital/inline_evolved_add_job_per_ascension_civic_regular
* jobs/capital/inline_evolved_add_job_civic_machine
* jobs/capital/inline_evolved_add_job_per_ascension_civic_hive
* jobs/capital/inline_evolved_add_job_per_ascension_civic_machine
* jobs/inline_evolved_healthcare
* jobs/inline_evolved_coordinator
* jobs/inline_evolved_farmer
* jobs/inline_evolved_prime_drone
* jobs/inline_evolved_farmer_secondary
* jobs/inline_evolved_researcher_swaps
* jobs/inline_evolved_clerk
* jobs/inline_evolved_technician_secondary
* jobs/inline_evolved_patrol_drone
* jobs/inline_evolved_priest_swaps
* jobs/inline_evolved_executive_civic_swaps
* jobs/inline_evolved_maintenance_civic_machine_swaps
* jobs/inline_evolved_enforcer
* jobs/inline_evolved_researcher
* jobs/inline_evolved_warrior_drone
* jobs/inline_evolved_maintenance_civic_hive_swaps
* jobs/inline_evolved_colonist
* jobs/inline_evolved_miner_secondary
* jobs/inline_evolved_politician_civic_swaps
* jobs/inline_evolved_maintenance_drone
* jobs/inline_evolved_entertainer
* jobs/inline_evolved_miner
* jobs/inline_evolved_synapse_civic_swaps
* jobs/inline_evolved_soldier
* mod_support/inline_evolved_spiritualist_cults
* buildings/convert_to/inline_evolved_research_3
* buildings/convert_to/inline_evolved_housing_1
* buildings/convert_to/inline_evolved_naval_academy_2
* buildings/convert_to/inline_evolved_monument_1
* buildings/convert_to/inline_evolved_temple_3
* buildings/convert_to/inline_evolved_capital_t4
* buildings/convert_to/inline_evolved_housing_2
* buildings/convert_to/inline_evolved_naval_academy_1
* buildings/convert_to/inline_evolved_capital_t2
* buildings/convert_to/inline_evolved_stronghold_3
* buildings/convert_to/inline_evolved_capital_t5
* buildings/convert_to/inline_evolved_temple_1
* buildings/convert_to/inline_evolved_bureaucratic_1
* buildings/convert_to/inline_evolved_bureaucratic_3
* buildings/convert_to/inline_evolved_stronghold_2
* buildings/convert_to/inline_evolved_research_1
* buildings/convert_to/inline_evolved_capital_t3
* buildings/convert_to/inline_evolved_bureaucratic_2
* buildings/convert_to/inline_evolved_monument_3
* buildings/convert_to/inline_evolved_naval_academy_3
* buildings/convert_to/inline_evolved_monument_2
* buildings/convert_to/inline_evolved_research_2
* buildings/convert_to/inline_evolved_capital_t1
* buildings/convert_to/inline_evolved_temple_2
* buildings/convert_to/inline_evolved_stronghold_1
* buildings/effects/type/inline_evolved_fortress
* buildings/effects/type/inline_evolved_fortress_machine
* buildings/effects/type/inline_evolved_bureaucratic_hive
* buildings/effects/type/inline_evolved_research_lab
* buildings/effects/type/inline_evolved_bureaucratic_machine
* buildings/effects/type/inline_evolved_research_lab_machine
* buildings/effects/type/inline_evolved_bureaucratic
* buildings/effects/type/inline_evolved_research_lab_hive
* buildings/effects/type/inline_evolved_fortress_hive
* buildings/effects/type/inline_evolved_temple
* buildings/effects/type/inline_evolved_monument
* buildings/effects/type/inline_evolved_monument_machine
* buildings/effects/type/inline_evolved_monument_regular
* buildings/effects/type/inline_evolved_bureaucratic_regular
* buildings/effects/type/inline_evolved_research_lab_regular
* buildings/effects/type/inline_evolved_monument_hive
* buildings/effects/type/inline_evolved_fortress_regular
* modifiers/inline_evolved_rural_mining_district_build_speed
* modifiers/inline_evolved_rural_generator_district_build_speed
* modifiers/inline_evolved_rural_mining_district_max
* modifiers/inline_evolved_rural_farming_district_build_speed
* modifiers/inline_evolved_rural_farming_district_max
* modifiers/inline_evolved_rural_generator_district_max
* capitals/inline_evolved_common_modifiers
* capitals/inline_evolved_colony_habitat
* capitals/inline_evolved_regular_capital
* capitals/inline_evolved_machine_capital
* capitals/inline_evolved_common_habitat_modifiers
* capitals/inline_evolved_colony
* capitals/inline_evolved_special_capital
* capitals/inline_evolved_all_capital
* capitals/inline_evolved_hive_capital
* districts/type/inline_evolved_housing_nexus
* districts/type/inline_evolved_housing_habitat
* districts/type/inline_evolved_rural_mining
* districts/type/inline_evolved_housing_hive
* districts/type/inline_evolved_housing_generic
* districts/type/inline_evolved_housing_city
* districts/type/inline_evolved_housing_arcology
* districts/type/inline_evolved_trade
* districts/type/inline_evolved_rural_generator
* districts/type/inline_evolved_rural_farming
* districts/type/inline_evolved_housing_nexus
* districts/type/inline_evolved_housing_habitat
* districts/type/inline_evolved_rural_mining
* districts/type/inline_evolved_housing_hive
* districts/type/inline_evolved_housing_generic
* districts/type/inline_evolved_housing_city
* districts/type/inline_evolved_housing_arcology
* districts/type/inline_evolved_trade
* districts/type/inline_evolved_rural_generator
* districts/type/inline_evolved_rural_farming
* jobs/inline_evolved_technician
* jobs/inline_evolved_priest
* jobs/capital/inline_evolved_add_ruler_civic_regular
* jobs/capital/inline_evolved_add_job_civic_hive
* jobs/capital/inline_evolved_add_job_civic_regular
* jobs/capital/inline_evolved_add_job_per_ascension_civic_regular
* jobs/capital/inline_evolved_add_job_civic_machine
* jobs/capital/inline_evolved_add_job_per_ascension_civic_hive
* jobs/capital/inline_evolved_add_job_per_ascension_civic_machine
* jobs/inline_evolved_healthcare
* jobs/inline_evolved_coordinator
* jobs/inline_evolved_farmer
* jobs/inline_evolved_prime_drone
* jobs/inline_evolved_farmer_secondary
* jobs/inline_evolved_researcher_swaps
* jobs/inline_evolved_clerk
* jobs/inline_evolved_technician_secondary
* jobs/inline_evolved_patrol_drone
* jobs/inline_evolved_priest_swaps
* jobs/inline_evolved_executive_civic_swaps
* jobs/inline_evolved_maintenance_civic_machine_swaps
* jobs/inline_evolved_enforcer
* jobs/inline_evolved_researcher
* jobs/inline_evolved_warrior_drone
* jobs/inline_evolved_maintenance_civic_hive_swaps
* jobs/inline_evolved_colonist
* jobs/inline_evolved_miner_secondary
* jobs/inline_evolved_politician_civic_swaps
* jobs/inline_evolved_maintenance_drone
* jobs/inline_evolved_entertainer
* jobs/inline_evolved_miner
* jobs/inline_evolved_synapse_civic_swaps
* jobs/inline_evolved_soldier
* jobs/capital/inline_evolved_add_ruler_civic_regular
* jobs/capital/inline_evolved_add_job_civic_hive
* jobs/capital/inline_evolved_add_job_civic_regular
* jobs/capital/inline_evolved_add_job_per_ascension_civic_regular
* jobs/capital/inline_evolved_add_job_civic_machine
* jobs/capital/inline_evolved_add_job_per_ascension_civic_hive
* jobs/capital/inline_evolved_add_job_per_ascension_civic_machine
* mod_support/inline_evolved_spiritualist_cults
* buildings/convert_to/inline_evolved_research_3
* buildings/convert_to/inline_evolved_housing_1
* buildings/convert_to/inline_evolved_naval_academy_2
* buildings/convert_to/inline_evolved_monument_1
* buildings/convert_to/inline_evolved_temple_3
* buildings/convert_to/inline_evolved_capital_t4
* buildings/convert_to/inline_evolved_housing_2
* buildings/convert_to/inline_evolved_naval_academy_1
* buildings/convert_to/inline_evolved_capital_t2
* buildings/convert_to/inline_evolved_stronghold_3
* buildings/convert_to/inline_evolved_capital_t5
* buildings/convert_to/inline_evolved_temple_1
* buildings/convert_to/inline_evolved_bureaucratic_1
* buildings/convert_to/inline_evolved_bureaucratic_3
* buildings/convert_to/inline_evolved_stronghold_2
* buildings/convert_to/inline_evolved_research_1
* buildings/convert_to/inline_evolved_capital_t3
* buildings/convert_to/inline_evolved_bureaucratic_2
* buildings/convert_to/inline_evolved_monument_3
* buildings/convert_to/inline_evolved_naval_academy_3
* buildings/convert_to/inline_evolved_monument_2
* buildings/convert_to/inline_evolved_research_2
* buildings/convert_to/inline_evolved_capital_t1
* buildings/convert_to/inline_evolved_temple_2
* buildings/convert_to/inline_evolved_stronghold_1
* buildings/effects/type/inline_evolved_fortress
* buildings/effects/type/inline_evolved_fortress_machine
* buildings/effects/type/inline_evolved_bureaucratic_hive
* buildings/effects/type/inline_evolved_research_lab
* buildings/effects/type/inline_evolved_bureaucratic_machine
* buildings/effects/type/inline_evolved_research_lab_machine
* buildings/effects/type/inline_evolved_bureaucratic
* buildings/effects/type/inline_evolved_research_lab_hive
* buildings/effects/type/inline_evolved_fortress_hive
* buildings/effects/type/inline_evolved_temple
* buildings/effects/type/inline_evolved_monument
* buildings/effects/type/inline_evolved_monument_machine
* buildings/effects/type/inline_evolved_monument_regular
* buildings/effects/type/inline_evolved_bureaucratic_regular
* buildings/effects/type/inline_evolved_research_lab_regular
* buildings/effects/type/inline_evolved_monument_hive
* buildings/effects/type/inline_evolved_fortress_regular
* buildings/convert_to/inline_evolved_research_3
* buildings/convert_to/inline_evolved_housing_1
* buildings/convert_to/inline_evolved_naval_academy_2
* buildings/convert_to/inline_evolved_monument_1
* buildings/convert_to/inline_evolved_temple_3
* buildings/convert_to/inline_evolved_capital_t4
* buildings/convert_to/inline_evolved_housing_2
* buildings/convert_to/inline_evolved_naval_academy_1
* buildings/convert_to/inline_evolved_capital_t2
* buildings/convert_to/inline_evolved_stronghold_3
* buildings/convert_to/inline_evolved_capital_t5
* buildings/convert_to/inline_evolved_temple_1
* buildings/convert_to/inline_evolved_bureaucratic_1
* buildings/convert_to/inline_evolved_bureaucratic_3
* buildings/convert_to/inline_evolved_stronghold_2
* buildings/convert_to/inline_evolved_research_1
* buildings/convert_to/inline_evolved_capital_t3
* buildings/convert_to/inline_evolved_bureaucratic_2
* buildings/convert_to/inline_evolved_monument_3
* buildings/convert_to/inline_evolved_naval_academy_3
* buildings/convert_to/inline_evolved_monument_2
* buildings/convert_to/inline_evolved_research_2
* buildings/convert_to/inline_evolved_capital_t1
* buildings/convert_to/inline_evolved_temple_2
* buildings/convert_to/inline_evolved_stronghold_1
* buildings/effects/type/inline_evolved_fortress
* buildings/effects/type/inline_evolved_fortress_machine
* buildings/effects/type/inline_evolved_bureaucratic_hive
* buildings/effects/type/inline_evolved_research_lab
* buildings/effects/type/inline_evolved_bureaucratic_machine
* buildings/effects/type/inline_evolved_research_lab_machine
* buildings/effects/type/inline_evolved_bureaucratic
* buildings/effects/type/inline_evolved_research_lab_hive
* buildings/effects/type/inline_evolved_fortress_hive
* buildings/effects/type/inline_evolved_temple
* buildings/effects/type/inline_evolved_monument
* buildings/effects/type/inline_evolved_monument_machine
* buildings/effects/type/inline_evolved_monument_regular
* buildings/effects/type/inline_evolved_bureaucratic_regular
* buildings/effects/type/inline_evolved_research_lab_regular
* buildings/effects/type/inline_evolved_monument_hive
* buildings/effects/type/inline_evolved_fortress_regular
* buildings/effects/type/inline_evolved_fortress
* buildings/effects/type/inline_evolved_fortress_machine
* buildings/effects/type/inline_evolved_bureaucratic_hive
* buildings/effects/type/inline_evolved_research_lab
* buildings/effects/type/inline_evolved_bureaucratic_machine
* buildings/effects/type/inline_evolved_research_lab_machine
* buildings/effects/type/inline_evolved_bureaucratic
* buildings/effects/type/inline_evolved_research_lab_hive
* buildings/effects/type/inline_evolved_fortress_hive
* buildings/effects/type/inline_evolved_temple
* buildings/effects/type/inline_evolved_monument
* buildings/effects/type/inline_evolved_monument_machine
* buildings/effects/type/inline_evolved_monument_regular
* buildings/effects/type/inline_evolved_bureaucratic_regular
* buildings/effects/type/inline_evolved_research_lab_regular
* buildings/effects/type/inline_evolved_monument_hive
* buildings/effects/type/inline_evolved_fortress_regular
* modifiers/inline_evolved_rural_mining_district_build_speed
* modifiers/inline_evolved_rural_generator_district_build_speed
* modifiers/inline_evolved_rural_mining_district_max
* modifiers/inline_evolved_rural_farming_district_build_speed
* modifiers/inline_evolved_rural_farming_district_max
* modifiers/inline_evolved_rural_generator_district_max
