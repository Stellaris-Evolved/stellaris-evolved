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

* [tec_blocks_industrial_designations](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L4579)
* [tec_blocks_non_industrial_designations](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L4594)
* [tec_blocks_regular_designations](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L4536)
* [tec_blocks_rural_designations](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L4565)
* [tec_blocks_urban_designations](common/scripted_triggers/zzz_evolved_scripted_triggers.txt#L4549)
* [tec_country_has_autocratic_authority](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1808)
* [tec_country_has_democratic_authority](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1787)
* [tec_country_has_oligarchic_authority](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1797)
* [tec_has_artisan_upkeep_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L458)
* [tec_has_artisan_upkeep_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L448)
* [tec_has_bureaucratic_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L354)
* [tec_has_clerk_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L55)
* [tec_has_clinic_building_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L167)
* [tec_has_colonist_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L39)
* [tec_has_coordinator_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L71)
* [tec_has_cyborg_clinic_exception](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L183)
* [tec_has_diplomatic_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1171)
* [tec_has_directive_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L604)
* [tec_has_enforcer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L23)
* [tec_has_entertainer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L7)
* [tec_has_farmer_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L214)
* [tec_has_farmer_production_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L479)
* [tec_has_farmer_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L468)
* [tec_has_farmer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L195)
* [tec_has_forced_living_standard_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L648)
* [tec_has_foundry_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L338)
* [tec_has_foundry_upkeep_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L438)
* [tec_has_foundry_upkeep_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L425)
* [tec_has_healthcare_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L150)
* [tec_has_maintenance_drone_swap_civic_hive](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L563)
* [tec_has_maintenance_drone_swap_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L631)
* [tec_has_maintenance_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L104)
* [tec_has_matter_miner](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L284)
* [tec_has_miner_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L249)
* [tec_has_miner_production_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L500)
* [tec_has_miner_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L489)
* [tec_has_miner_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L231)
* [tec_has_monument_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L379)
* [tec_has_naval_academy_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L414)
* [tec_has_patrol_drone_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L119)
* [tec_has_research_lab_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L391)
* [tec_has_ruler_civic_hive](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L540)
* [tec_has_ruler_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L579)
* [tec_has_ruler_civic_mega](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L512)
* [tec_has_ruler_civic_regular](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L425)
* [tec_has_scrap_miner](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L502)
* [tec_has_slaver_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1147)
* [tec_has_soldier_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L87)
* [tec_has_special_ruler_feature](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L380)
* [tec_has_spy_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1161)
* [tec_has_stronghold_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L402)
* [tec_has_technician_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L322)
* [tec_has_technician_production_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L523)
* [tec_has_technician_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L512)
* [tec_has_technician_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L304)
* [tec_has_temple_swap_exception](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L532)
* [tec_has_warrior_drone_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L134)
* [tec_is_special_researcher_empire](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L161)
* [tec_is_spiritualist_main_cult](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L333)
* [tec_is_spiritualist_secondary_cult](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L356)
* [tec_replaces_half_researcher_empire](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L184)

## Current supported scripted_effects

* [tec_cache_building_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L232)
* [tec_cache_capital_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L176)
* [tec_cache_colony_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L311)
* [tec_cache_combined_values](common/scripted_effects/zz_evolved_scripted_effects.txt#L259)
* [tec_cache_country_civic_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L671)
* [tec_cache_country_monthly_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L574)
* [tec_cache_planet_type_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L43)
* [tec_cache_pop_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L430)
* [tec_cache_species_traits_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L534)

## Current supported scripted_effects

* [crystals_buildings_value](common/script_values/zz_evolved_script_values.txt#L1236)
* [farming_buildings_value](common/script_values/zz_evolved_script_values.txt#L1018)
* [farming_combined_value](common/script_values/zz_evolved_script_values.txt#L1488)
* [farming_districts_value](common/script_values/zz_evolved_script_values.txt#L386)
* [gases_buildings_value](common/script_values/zz_evolved_script_values.txt#L1271)
* [generator_buildings_value](common/script_values/zz_evolved_script_values.txt#L1108)
* [generator_combined_value](common/script_values/zz_evolved_script_values.txt#L1548)
* [generator_districts_value](common/script_values/zz_evolved_script_values.txt#L479)
* [housing_districts_value](common/script_values/zz_evolved_script_values.txt#L732)
* [industrial_districts_value](common/script_values/zz_evolved_script_values.txt#L539)
* [leisure_district_value](common/script_values/zz_evolved_script_values.txt#L980)
* [military_combined_value](common/script_values/zz_evolved_script_values.txt#L1722)
* [mining_buildings_value](common/script_values/zz_evolved_script_values.txt#L1070)
* [mining_combined_value](common/script_values/zz_evolved_script_values.txt#L1518)
* [mining_districts_value](common/script_values/zz_evolved_script_values.txt#L432)
* [motes_buildings_value](common/script_values/zz_evolved_script_values.txt#L1200)
* [refinery_combined_value](common/script_values/zz_evolved_script_values.txt#L1639)
* [research_buildings_value](common/script_values/zz_evolved_script_values.txt#L1150)
* [research_combined_value](common/script_values/zz_evolved_script_values.txt#L1578)
* [research_districts_value](common/script_values/zz_evolved_script_values.txt#L665)
* [stronghold_buildings_value](common/script_values/zz_evolved_script_values.txt#L1307)
* [tec_district_farming_max_value](common/script_values/zz_evolved_script_values.txt#L2088)
* [tec_district_generator_max_value](common/script_values/zz_evolved_script_values.txt#L2130)
* [tec_district_mining_max_value](common/script_values/zz_evolved_script_values.txt#L2109)
* [tec_farmer_jobs_value](common/script_values/zz_evolved_script_values.txt#L2063)
* [tec_priest_jobs_value](common/script_values/zz_evolved_script_values.txt#L1957)
* [tec_researcher_jobs_value](common/script_values/zz_evolved_script_values.txt#L1892)
* [tec_soldier_jobs_value](common/script_values/zz_evolved_script_values.txt#L1996)
* [tec_trader_jobs_value](common/script_values/zz_evolved_script_values.txt#L2040)
* [trade_building_value](common/script_values/zz_evolved_script_values.txt#L1459)
* [trade_combined_value](common/script_values/zz_evolved_script_values.txt#L1693)
* [trade_districts_value](common/script_values/zz_evolved_script_values.txt#L944)
* [unity_buildings_value](common/script_values/zz_evolved_script_values.txt#L1355)
* [unity_combined_value](common/script_values/zz_evolved_script_values.txt#L1608)
* [unity_districts_value](common/script_values/zz_evolved_script_values.txt#L823)
* [unity_servitor_specific_districts_value](common/script_values/zz_evolved_script_values.txt#L907)
* [virtuality_concentrated_production_mult](common/script_values/zz_ow_04_script_values_machine_age.txt#L1)
* [virtuality_num_colonies](common/script_values/zz_ow_04_script_values_machine_age.txt#L17)

## Current supported inline_scripts

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
* [buildings/convert_to/tec_housing_1](common/inline_scripts/buildings/convert_to/tec_housing_1.txt#L17)
* [buildings/convert_to/tec_housing_2](common/inline_scripts/buildings/convert_to/tec_housing_2.txt#L17)
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
* [buildings/effects/type/tec_bureaucratic](common/inline_scripts/buildings/effects/type/tec_bureaucratic.txt#L23)
* [buildings/effects/type/tec_bureaucratic_hive](common/inline_scripts/buildings/effects/type/tec_bureaucratic_hive.txt#L14)
* [buildings/effects/type/tec_bureaucratic_machine](common/inline_scripts/buildings/effects/type/tec_bureaucratic_machine.txt#L5)
* [buildings/effects/type/tec_bureaucratic_regular](common/inline_scripts/buildings/effects/type/tec_bureaucratic_regular.txt#L19)
* [buildings/effects/type/tec_chemical_plant](common/inline_scripts/buildings/effects/type/tec_chemical_plant.txt#L10)
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
* [buildings/effects/type/tec_healthcare](common/inline_scripts/buildings/effects/type/tec_healthcare.txt#L33)
* [buildings/effects/type/tec_hydroponics_farm](common/inline_scripts/buildings/effects/type/tec_hydroponics_farm.txt#L10)
* [buildings/effects/type/tec_military_booster](common/inline_scripts/buildings/effects/type/tec_military_booster.txt#L13)
* [buildings/effects/type/tec_mineral_purification_plant](common/inline_scripts/buildings/effects/type/tec_mineral_purification_plant.txt#L69)
* [buildings/effects/type/tec_ministry_production](common/inline_scripts/buildings/effects/type/tec_ministry_production.txt#L10)
* [buildings/effects/type/tec_monument](common/inline_scripts/buildings/effects/type/tec_monument.txt#L16)
* [buildings/effects/type/tec_monument_hive](common/inline_scripts/buildings/effects/type/tec_monument_hive.txt#L6)
* [buildings/effects/type/tec_monument_machine](common/inline_scripts/buildings/effects/type/tec_monument_machine.txt#L6)
* [buildings/effects/type/tec_monument_regular](common/inline_scripts/buildings/effects/type/tec_monument_regular.txt#L5)
* [buildings/effects/type/tec_naval_academy](common/inline_scripts/buildings/effects/type/tec_naval_academy.txt#L16)
* [buildings/effects/type/tec_naval_academy_hive](common/inline_scripts/buildings/effects/type/tec_naval_academy_hive.txt#L5)
* [buildings/effects/type/tec_naval_academy_machine](common/inline_scripts/buildings/effects/type/tec_naval_academy_machine.txt#L5)
* [buildings/effects/type/tec_naval_academy_regular](common/inline_scripts/buildings/effects/type/tec_naval_academy_regular.txt#L7)
* [buildings/effects/type/tec_refinery](common/inline_scripts/buildings/effects/type/tec_refinery.txt#L10)
* [buildings/effects/type/tec_research_lab](common/inline_scripts/buildings/effects/type/tec_research_lab.txt#L38)
* [buildings/effects/type/tec_research_lab_hive](common/inline_scripts/buildings/effects/type/tec_research_lab_hive.txt#L5)
* [buildings/effects/type/tec_research_lab_machine](common/inline_scripts/buildings/effects/type/tec_research_lab_machine.txt#L6)
* [buildings/effects/type/tec_research_lab_regular](common/inline_scripts/buildings/effects/type/tec_research_lab_regular.txt#L16)
* [buildings/effects/type/tec_resource_silo](common/inline_scripts/buildings/effects/type/tec_resource_silo.txt#L15)
* [buildings/effects/type/tec_robot_assembly](common/inline_scripts/buildings/effects/type/tec_robot_assembly.txt#L27)
* [buildings/effects/type/tec_robot_assembly_hive](common/inline_scripts/buildings/effects/type/tec_robot_assembly_hive.txt#L10)
* [buildings/effects/type/tec_robot_assembly_machine](common/inline_scripts/buildings/effects/type/tec_robot_assembly_machine.txt#L10)
* [buildings/effects/type/tec_robot_assembly_regular](common/inline_scripts/buildings/effects/type/tec_robot_assembly_regular.txt#L17)
* [buildings/effects/type/tec_stripmine](common/inline_scripts/buildings/effects/type/tec_stripmine.txt#L10)
* [buildings/effects/type/tec_temple](common/inline_scripts/buildings/effects/type/tec_temple.txt#L20)
* [buildings/effects/type/tec_trade](common/inline_scripts/buildings/effects/type/tec_trade.txt#L22)
* [buildings/effects/type/tec_trade_hive](common/inline_scripts/buildings/effects/type/tec_trade_hive.txt#L5)
* [buildings/effects/type/tec_trade_machine](common/inline_scripts/buildings/effects/type/tec_trade_machine.txt#L5)
* [buildings/effects/type/tec_trade_regular](common/inline_scripts/buildings/effects/type/tec_trade_regular.txt#L17)
* [capitals/tec_all_capital](common/inline_scripts/capitals/tec_all_capital.txt#L48)
* [capitals/tec_colony](common/inline_scripts/capitals/tec_colony.txt#L13)
* [capitals/tec_colony_habitat](common/inline_scripts/capitals/tec_colony_habitat.txt#L14)
* [capitals/tec_common_habitat_modifiers](common/inline_scripts/capitals/tec_common_habitat_modifiers.txt#L88)
* [capitals/tec_common_modifiers](common/inline_scripts/capitals/tec_common_modifiers.txt#L13)
* [capitals/tec_hive_capital](common/inline_scripts/capitals/tec_hive_capital.txt#L117)
* [capitals/tec_machine_capital](common/inline_scripts/capitals/tec_machine_capital.txt#L103)
* [capitals/tec_regular_capital](common/inline_scripts/capitals/tec_regular_capital.txt#L146)
* [capitals/tec_special_capital](common/inline_scripts/capitals/tec_special_capital.txt#L31)
* [districts/type/tec_housing_arcology](common/inline_scripts/districts/type/tec_housing_arcology.txt#L36)
* [districts/type/tec_housing_city](common/inline_scripts/districts/type/tec_housing_city.txt#L26)
* [districts/type/tec_housing_generic](common/inline_scripts/districts/type/tec_housing_generic.txt#L22)
* [districts/type/tec_housing_habitat](common/inline_scripts/districts/type/tec_housing_habitat.txt#L49)
* [districts/type/tec_housing_hive](common/inline_scripts/districts/type/tec_housing_hive.txt#L24)
* [districts/type/tec_housing_nexus](common/inline_scripts/districts/type/tec_housing_nexus.txt#L35)
* [districts/type/tec_maintenance](common/inline_scripts/districts/type/tec_maintenance.txt#L20)
* [districts/type/tec_research](common/inline_scripts/districts/type/tec_research.txt#L22)
* [districts/type/tec_rural_farming](common/inline_scripts/districts/type/tec_rural_farming.txt#L119)
* [districts/type/tec_rural_generator](common/inline_scripts/districts/type/tec_rural_generator.txt#L106)
* [districts/type/tec_rural_mining](common/inline_scripts/districts/type/tec_rural_mining.txt#L117)
* [districts/type/tec_trade](common/inline_scripts/districts/type/tec_trade.txt#L38)
* [districts/type/tec_unity](common/inline_scripts/districts/type/tec_unity.txt#L22)
* [jobs/capital/tec_add_job_civic_hive](common/inline_scripts/jobs/capital/tec_add_job_civic_hive.txt#L25)
* [jobs/capital/tec_add_job_civic_machine](common/inline_scripts/jobs/capital/tec_add_job_civic_machine.txt#L25)
* [jobs/capital/tec_add_job_civic_regular](common/inline_scripts/jobs/capital/tec_add_job_civic_regular.txt#L152)
* [jobs/capital/tec_add_job_per_ascension_civic_hive](common/inline_scripts/jobs/capital/tec_add_job_per_ascension_civic_hive.txt#L58)
* [jobs/capital/tec_add_job_per_ascension_civic_machine](common/inline_scripts/jobs/capital/tec_add_job_per_ascension_civic_machine.txt#L22)
* [jobs/capital/tec_add_job_per_ascension_civic_regular](common/inline_scripts/jobs/capital/tec_add_job_per_ascension_civic_regular.txt#L5)
* [jobs/capital/tec_add_ruler_civic_regular](common/inline_scripts/jobs/capital/tec_add_ruler_civic_regular.txt#L111)
* [jobs/tec_clerk](common/inline_scripts/jobs/tec_clerk.txt#L40)
* [jobs/tec_colonist](common/inline_scripts/jobs/tec_colonist.txt#L23)
* [jobs/tec_coordinator](common/inline_scripts/jobs/tec_coordinator.txt#L28)
* [jobs/tec_enforcer](common/inline_scripts/jobs/tec_enforcer.txt#L24)
* [jobs/tec_entertainer](common/inline_scripts/jobs/tec_entertainer.txt#L41)
* [jobs/tec_executive_civic_swaps](common/inline_scripts/jobs/tec_executive_civic_swaps.txt#L162)
* [jobs/tec_farmer](common/inline_scripts/jobs/tec_farmer.txt#L124)
* [jobs/tec_farmer_secondary](common/inline_scripts/jobs/tec_farmer_secondary.txt#L51)
* [jobs/tec_foundry](common/inline_scripts/jobs/tec_foundry.txt#L153)
* [jobs/tec_healthcare](common/inline_scripts/jobs/tec_healthcare.txt#L59)
* [jobs/tec_maintenance_civic_hive_swaps](common/inline_scripts/jobs/tec_maintenance_civic_hive_swaps.txt#L25)
* [jobs/tec_maintenance_civic_machine_swaps](common/inline_scripts/jobs/tec_maintenance_civic_machine_swaps.txt#L6)
* [jobs/tec_maintenance_drone](common/inline_scripts/jobs/tec_maintenance_drone.txt#L26)
* [jobs/tec_miner](common/inline_scripts/jobs/tec_miner.txt#L230)
* [jobs/tec_miner_secondary](common/inline_scripts/jobs/tec_miner_secondary.txt#L53)
* [jobs/tec_patrol_drone](common/inline_scripts/jobs/tec_patrol_drone.txt#L26)
* [jobs/tec_politician_civic_swaps](common/inline_scripts/jobs/tec_politician_civic_swaps.txt#L248)
* [jobs/tec_priest](common/inline_scripts/jobs/tec_priest.txt#L160)
* [jobs/tec_priest_swaps](common/inline_scripts/jobs/tec_priest_swaps.txt#L92)
* [jobs/tec_prime_drone](common/inline_scripts/jobs/tec_prime_drone.txt#L166)
* [jobs/tec_researcher](common/inline_scripts/jobs/tec_researcher.txt#L178)
* [jobs/tec_researcher_swaps](common/inline_scripts/jobs/tec_researcher_swaps.txt#L75)
* [jobs/tec_soldier](common/inline_scripts/jobs/tec_soldier.txt#L60)
* [jobs/tec_spawning_drone](common/inline_scripts/jobs/tec_spawning_drone.txt#L42)
* [jobs/tec_synapse_civic_swaps](common/inline_scripts/jobs/tec_synapse_civic_swaps.txt#L78)
* [jobs/tec_technician](common/inline_scripts/jobs/tec_technician.txt#L104)
* [jobs/tec_technician_secondary](common/inline_scripts/jobs/tec_technician_secondary.txt#L34)
* [jobs/tec_warrior_drone](common/inline_scripts/jobs/tec_warrior_drone.txt#L25)
* [mod_support/tec_$authority$_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_corporate_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_democratic_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_dictatorial_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_hive_mind_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_imperial_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_machine_intelligence_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_oligarchic_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_tec_ai_corporate_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_tec_ai_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_tec_hive_biological_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_tec_hive_biomechanical_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_tec_hive_cybernetic_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_tec_machine_consensus_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_tec_patrocorporate_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_auth_tec_theocracy_swaps](common/inline_scripts/mod_support/tec_auth_swaps.txt#L10)
* [mod_support/tec_spiritualist_cults](common/inline_scripts/mod_support/tec_spiritualist_cults.txt#L5)
* [modifiers/tec_artisan_efficiency](common/inline_scripts/modifiers/tec_artisan_efficiency.txt#L96)
* [modifiers/tec_farmer_efficiency](common/inline_scripts/modifiers/tec_farmer_efficiency.txt#L26)
* [modifiers/tec_foundry_efficiency](common/inline_scripts/modifiers/tec_foundry_efficiency.txt#L82)
* [modifiers/tec_miner_efficiency](common/inline_scripts/modifiers/tec_miner_efficiency.txt#L62)
* [modifiers/tec_rural_farming_district_build_speed](common/inline_scripts/modifiers/tec_rural_farming_district_build_speed.txt#L122)
* [modifiers/tec_rural_farming_district_max](common/inline_scripts/modifiers/tec_rural_farming_district_max.txt#L20)
* [modifiers/tec_rural_generator_district_build_speed](common/inline_scripts/modifiers/tec_rural_generator_district_build_speed.txt#L122)
* [modifiers/tec_rural_generator_district_max](common/inline_scripts/modifiers/tec_rural_generator_district_max.txt#L20)
* [modifiers/tec_rural_mining_district_build_speed](common/inline_scripts/modifiers/tec_rural_mining_district_build_speed.txt#L122)
* [modifiers/tec_rural_mining_district_max](common/inline_scripts/modifiers/tec_rural_mining_district_max.txt#L20)
* [modifiers/tec_technician_efficiency](common/inline_scripts/modifiers/tec_technician_efficiency.txt#L26)
