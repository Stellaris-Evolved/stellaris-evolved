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

* [tec_has_artisan_upkeep_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L429)
* [tec_has_artisan_upkeep_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L420)
* [tec_has_bureaucratic_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L333)
* [tec_has_clerk_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L52)
* [tec_has_clinic_building_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L157)
* [tec_has_colonist_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L37)
* [tec_has_coordinator_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L67)
* [tec_has_cyborg_clinic_exception](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L172)
* [tec_has_diplomatic_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1093)
* [tec_has_directive_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L551)
* [tec_has_enforcer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L22)
* [tec_has_entertainer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L7)
* [tec_has_farmer_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L201)
* [tec_has_farmer_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L438)
* [tec_has_farmer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L183)
* [tec_has_forced_living_standard_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L593)
* [tec_has_foundry_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L318)
* [tec_has_foundry_upkeep_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L411)
* [tec_has_foundry_upkeep_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L399)
* [tec_has_healthcare_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L141)
* [tec_has_maintenance_drone_swap_civic_hive](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L511)
* [tec_has_maintenance_drone_swap_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L577)
* [tec_has_maintenance_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L98)
* [tec_has_matter_miner](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L267)
* [tec_has_miner_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L234)
* [tec_has_miner_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L457)
* [tec_has_miner_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L217)
* [tec_has_monument_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L357)
* [tec_has_naval_academy_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L389)
* [tec_has_patrol_drone_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L112)
* [tec_has_research_lab_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L368)
* [tec_has_ruler_civic_hive](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L489)
* [tec_has_ruler_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L526)
* [tec_has_ruler_civic_mega](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L462)
* [tec_has_ruler_civic_regular](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L376)
* [tec_has_scrap_miner](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L469)
* [tec_has_slaver_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1071)
* [tec_has_soldier_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L82)
* [tec_has_special_ruler_feature](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L337)
* [tec_has_spy_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1084)
* [tec_has_stronghold_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L378)
* [tec_has_technician_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L303)
* [tec_has_technician_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L478)
* [tec_has_technician_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L286)
* [tec_has_warrior_drone_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L126)
* [tec_is_special_researcher_empire](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L123)
* [tec_is_spiritualist_main_cult](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L293)
* [tec_is_spiritualist_secondary_cult](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L313)
* [tec_replaces_half_researcher_empire](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L145)

## Current supported scripted_effects

* [tec_cache_building_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L190)
* [tec_cache_capital_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L152)
* [tec_cache_colony_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L198)
* [tec_cache_country_civic_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L365)
* [tec_cache_country_councilor_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L573)
* [tec_cache_country_monthly_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L301)
* [tec_cache_planet_type_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L37)
* [tec_cache_pop_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L235)
* [tec_cache_species_traits_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L279)

## Current supported inline_scripts

* [buildings/convert_to/inline_evolved_assembly_bioservant_1](common/inline_scripts/buildings/convert_to/inline_evolved_assembly_bioservant_1.txt)
* [buildings/convert_to/inline_evolved_assembly_bioservant_2](common/inline_scripts/buildings/convert_to/inline_evolved_assembly_bioservant_2.txt)
* [buildings/convert_to/inline_evolved_assembly_bioservant_3](common/inline_scripts/buildings/convert_to/inline_evolved_assembly_bioservant_3.txt)
* [buildings/convert_to/inline_evolved_assembly_organic_1](common/inline_scripts/buildings/convert_to/inline_evolved_assembly_organic_1.txt)
* [buildings/convert_to/inline_evolved_assembly_organic_2](common/inline_scripts/buildings/convert_to/inline_evolved_assembly_organic_2.txt)
* [buildings/convert_to/inline_evolved_assembly_organic_3](common/inline_scripts/buildings/convert_to/inline_evolved_assembly_organic_3.txt)
* [buildings/convert_to/inline_evolved_assembly_robotic_1](common/inline_scripts/buildings/convert_to/inline_evolved_assembly_robotic_1.txt)
* [buildings/convert_to/inline_evolved_assembly_robotic_2](common/inline_scripts/buildings/convert_to/inline_evolved_assembly_robotic_2.txt)
* [buildings/convert_to/inline_evolved_assembly_robotic_3](common/inline_scripts/buildings/convert_to/inline_evolved_assembly_robotic_3.txt)
* [buildings/convert_to/inline_evolved_bureaucratic_1](common/inline_scripts/buildings/convert_to/inline_evolved_bureaucratic_1.txt)
* [buildings/convert_to/inline_evolved_bureaucratic_2](common/inline_scripts/buildings/convert_to/inline_evolved_bureaucratic_2.txt)
* [buildings/convert_to/inline_evolved_bureaucratic_3](common/inline_scripts/buildings/convert_to/inline_evolved_bureaucratic_3.txt)
* [buildings/convert_to/inline_evolved_capital_t1](common/inline_scripts/buildings/convert_to/inline_evolved_capital_t1.txt)
* [buildings/convert_to/inline_evolved_capital_t2](common/inline_scripts/buildings/convert_to/inline_evolved_capital_t2.txt)
* [buildings/convert_to/inline_evolved_capital_t3](common/inline_scripts/buildings/convert_to/inline_evolved_capital_t3.txt)
* [buildings/convert_to/inline_evolved_capital_t4](common/inline_scripts/buildings/convert_to/inline_evolved_capital_t4.txt)
* [buildings/convert_to/inline_evolved_capital_t5](common/inline_scripts/buildings/convert_to/inline_evolved_capital_t5.txt)
* [buildings/convert_to/inline_evolved_clinic_1](common/inline_scripts/buildings/convert_to/inline_evolved_clinic_1.txt)
* [buildings/convert_to/inline_evolved_clinic_2](common/inline_scripts/buildings/convert_to/inline_evolved_clinic_2.txt)
* [buildings/convert_to/inline_evolved_clinic_3](common/inline_scripts/buildings/convert_to/inline_evolved_clinic_3.txt)
* [buildings/convert_to/inline_evolved_housing_1](common/inline_scripts/buildings/convert_to/inline_evolved_housing_1.txt)
* [buildings/convert_to/inline_evolved_housing_2](common/inline_scripts/buildings/convert_to/inline_evolved_housing_2.txt)
* [buildings/convert_to/inline_evolved_monument_1](common/inline_scripts/buildings/convert_to/inline_evolved_monument_1.txt)
* [buildings/convert_to/inline_evolved_monument_2](common/inline_scripts/buildings/convert_to/inline_evolved_monument_2.txt)
* [buildings/convert_to/inline_evolved_monument_3](common/inline_scripts/buildings/convert_to/inline_evolved_monument_3.txt)
* [buildings/convert_to/inline_evolved_naval_academy_1](common/inline_scripts/buildings/convert_to/inline_evolved_naval_academy_1.txt)
* [buildings/convert_to/inline_evolved_naval_academy_2](common/inline_scripts/buildings/convert_to/inline_evolved_naval_academy_2.txt)
* [buildings/convert_to/inline_evolved_naval_academy_3](common/inline_scripts/buildings/convert_to/inline_evolved_naval_academy_3.txt)
* [buildings/convert_to/inline_evolved_research_1](common/inline_scripts/buildings/convert_to/inline_evolved_research_1.txt)
* [buildings/convert_to/inline_evolved_research_2](common/inline_scripts/buildings/convert_to/inline_evolved_research_2.txt)
* [buildings/convert_to/inline_evolved_research_3](common/inline_scripts/buildings/convert_to/inline_evolved_research_3.txt)
* [buildings/convert_to/inline_evolved_stronghold_1](common/inline_scripts/buildings/convert_to/inline_evolved_stronghold_1.txt)
* [buildings/convert_to/inline_evolved_stronghold_2](common/inline_scripts/buildings/convert_to/inline_evolved_stronghold_2.txt)
* [buildings/convert_to/inline_evolved_stronghold_3](common/inline_scripts/buildings/convert_to/inline_evolved_stronghold_3.txt)
* [buildings/convert_to/inline_evolved_temple_1](common/inline_scripts/buildings/convert_to/inline_evolved_temple_1.txt)
* [buildings/convert_to/inline_evolved_temple_2](common/inline_scripts/buildings/convert_to/inline_evolved_temple_2.txt)
* [buildings/convert_to/inline_evolved_temple_3](common/inline_scripts/buildings/convert_to/inline_evolved_temple_3.txt)
* [buildings/effects/type/inline_evolved_bureaucratic](common/inline_scripts/buildings/effects/type/inline_evolved_bureaucratic.txt)
* [buildings/effects/type/inline_evolved_bureaucratic_hive](common/inline_scripts/buildings/effects/type/inline_evolved_bureaucratic_hive.txt)
* [buildings/effects/type/inline_evolved_bureaucratic_machine](common/inline_scripts/buildings/effects/type/inline_evolved_bureaucratic_machine.txt)
* [buildings/effects/type/inline_evolved_bureaucratic_regular](common/inline_scripts/buildings/effects/type/inline_evolved_bureaucratic_regular.txt)
* [buildings/effects/type/inline_evolved_chemical_plant](common/inline_scripts/buildings/effects/type/inline_evolved_chemical_plant.txt)
* [buildings/effects/type/inline_evolved_crystal_plant](common/inline_scripts/buildings/effects/type/inline_evolved_crystal_plant.txt)
* [buildings/effects/type/inline_evolved_energy_grid](common/inline_scripts/buildings/effects/type/inline_evolved_energy_grid.txt)
* [buildings/effects/type/inline_evolved_factory](common/inline_scripts/buildings/effects/type/inline_evolved_factory.txt)
* [buildings/effects/type/inline_evolved_food_processing_facility](common/inline_scripts/buildings/effects/type/inline_evolved_food_processing_facility.txt)
* [buildings/effects/type/inline_evolved_fortress](common/inline_scripts/buildings/effects/type/inline_evolved_fortress.txt)
* [buildings/effects/type/inline_evolved_fortress_hive](common/inline_scripts/buildings/effects/type/inline_evolved_fortress_hive.txt)
* [buildings/effects/type/inline_evolved_fortress_machine](common/inline_scripts/buildings/effects/type/inline_evolved_fortress_machine.txt)
* [buildings/effects/type/inline_evolved_fortress_regular](common/inline_scripts/buildings/effects/type/inline_evolved_fortress_regular.txt)
* [buildings/effects/type/inline_evolved_foundry](common/inline_scripts/buildings/effects/type/inline_evolved_foundry.txt)
* [buildings/effects/type/inline_evolved_healthcare](common/inline_scripts/buildings/effects/type/inline_evolved_healthcare.txt)
* [buildings/effects/type/inline_evolved_hydroponics_farm](common/inline_scripts/buildings/effects/type/inline_evolved_hydroponics_farm.txt)
* [buildings/effects/type/inline_evolved_military_academy](common/inline_scripts/buildings/effects/type/inline_evolved_military_academy.txt)
* [buildings/effects/type/inline_evolved_mineral_purification_plant](common/inline_scripts/buildings/effects/type/inline_evolved_mineral_purification_plant.txt)
* [buildings/effects/type/inline_evolved_ministry_production](common/inline_scripts/buildings/effects/type/inline_evolved_ministry_production.txt)
* [buildings/effects/type/inline_evolved_monument](common/inline_scripts/buildings/effects/type/inline_evolved_monument.txt)
* [buildings/effects/type/inline_evolved_monument_hive](common/inline_scripts/buildings/effects/type/inline_evolved_monument_hive.txt)
* [buildings/effects/type/inline_evolved_monument_machine](common/inline_scripts/buildings/effects/type/inline_evolved_monument_machine.txt)
* [buildings/effects/type/inline_evolved_monument_regular](common/inline_scripts/buildings/effects/type/inline_evolved_monument_regular.txt)
* [buildings/effects/type/inline_evolved_naval_academy](common/inline_scripts/buildings/effects/type/inline_evolved_naval_academy.txt)
* [buildings/effects/type/inline_evolved_naval_academy_hive](common/inline_scripts/buildings/effects/type/inline_evolved_naval_academy_hive.txt)
* [buildings/effects/type/inline_evolved_naval_academy_machine](common/inline_scripts/buildings/effects/type/inline_evolved_naval_academy_machine.txt)
* [buildings/effects/type/inline_evolved_naval_academy_regular](common/inline_scripts/buildings/effects/type/inline_evolved_naval_academy_regular.txt)
* [buildings/effects/type/inline_evolved_refinery](common/inline_scripts/buildings/effects/type/inline_evolved_refinery.txt)
* [buildings/effects/type/inline_evolved_research_lab](common/inline_scripts/buildings/effects/type/inline_evolved_research_lab.txt)
* [buildings/effects/type/inline_evolved_research_lab_hive](common/inline_scripts/buildings/effects/type/inline_evolved_research_lab_hive.txt)
* [buildings/effects/type/inline_evolved_research_lab_machine](common/inline_scripts/buildings/effects/type/inline_evolved_research_lab_machine.txt)
* [buildings/effects/type/inline_evolved_research_lab_regular](common/inline_scripts/buildings/effects/type/inline_evolved_research_lab_regular.txt)
* [buildings/effects/type/inline_evolved_resource_silo](common/inline_scripts/buildings/effects/type/inline_evolved_resource_silo.txt)
* [buildings/effects/type/inline_evolved_tec_energrid](common/inline_scripts/buildings/effects/type/inline_evolved_tec_energrid.txt)
* [buildings/effects/type/inline_evolved_tec_stripmine](common/inline_scripts/buildings/effects/type/inline_evolved_tec_stripmine.txt)
* [buildings/effects/type/inline_evolved_temple](common/inline_scripts/buildings/effects/type/inline_evolved_temple.txt)
* [capitals/inline_evolved_all_capital](common/inline_scripts/capitals/inline_evolved_all_capital.txt)
* [capitals/inline_evolved_colony](common/inline_scripts/capitals/inline_evolved_colony.txt)
* [capitals/inline_evolved_colony_habitat](common/inline_scripts/capitals/inline_evolved_colony_habitat.txt)
* [capitals/inline_evolved_common_habitat_modifiers](common/inline_scripts/capitals/inline_evolved_common_habitat_modifiers.txt)
* [capitals/inline_evolved_common_modifiers](common/inline_scripts/capitals/inline_evolved_common_modifiers.txt)
* [capitals/inline_evolved_hive_capital](common/inline_scripts/capitals/inline_evolved_hive_capital.txt)
* [capitals/inline_evolved_machine_capital](common/inline_scripts/capitals/inline_evolved_machine_capital.txt)
* [capitals/inline_evolved_regular_capital](common/inline_scripts/capitals/inline_evolved_regular_capital.txt)
* [capitals/inline_evolved_special_capital](common/inline_scripts/capitals/inline_evolved_special_capital.txt)
* [districts/type/inline_evolved_housing_arcology](common/inline_scripts/districts/type/inline_evolved_housing_arcology.txt)
* [districts/type/inline_evolved_housing_city](common/inline_scripts/districts/type/inline_evolved_housing_city.txt)
* [districts/type/inline_evolved_housing_generic](common/inline_scripts/districts/type/inline_evolved_housing_generic.txt)
* [districts/type/inline_evolved_housing_habitat](common/inline_scripts/districts/type/inline_evolved_housing_habitat.txt)
* [districts/type/inline_evolved_housing_hive](common/inline_scripts/districts/type/inline_evolved_housing_hive.txt)
* [districts/type/inline_evolved_housing_nexus](common/inline_scripts/districts/type/inline_evolved_housing_nexus.txt)
* [districts/type/inline_evolved_rural_farming](common/inline_scripts/districts/type/inline_evolved_rural_farming.txt)
* [districts/type/inline_evolved_rural_generator](common/inline_scripts/districts/type/inline_evolved_rural_generator.txt)
* [districts/type/inline_evolved_rural_mining](common/inline_scripts/districts/type/inline_evolved_rural_mining.txt)
* [districts/type/inline_evolved_trade](common/inline_scripts/districts/type/inline_evolved_trade.txt)
* [jobs/capital/inline_evolved_add_job_civic_hive](common/inline_scripts/jobs/capital/inline_evolved_add_job_civic_hive.txt)
* [jobs/capital/inline_evolved_add_job_civic_machine](common/inline_scripts/jobs/capital/inline_evolved_add_job_civic_machine.txt)
* [jobs/capital/inline_evolved_add_job_civic_regular](common/inline_scripts/jobs/capital/inline_evolved_add_job_civic_regular.txt)
* [jobs/capital/inline_evolved_add_job_per_ascension_civic_hive](common/inline_scripts/jobs/capital/inline_evolved_add_job_per_ascension_civic_hive.txt)
* [jobs/capital/inline_evolved_add_job_per_ascension_civic_machine](common/inline_scripts/jobs/capital/inline_evolved_add_job_per_ascension_civic_machine.txt)
* [jobs/capital/inline_evolved_add_job_per_ascension_civic_regular](common/inline_scripts/jobs/capital/inline_evolved_add_job_per_ascension_civic_regular.txt)
* [jobs/capital/inline_evolved_add_ruler_civic_regular](common/inline_scripts/jobs/capital/inline_evolved_add_ruler_civic_regular.txt)
* [jobs/inline_evolved_clerk](common/inline_scripts/jobs/inline_evolved_clerk.txt)
* [jobs/inline_evolved_colonist](common/inline_scripts/jobs/inline_evolved_colonist.txt)
* [jobs/inline_evolved_coordinator](common/inline_scripts/jobs/inline_evolved_coordinator.txt)
* [jobs/inline_evolved_enforcer](common/inline_scripts/jobs/inline_evolved_enforcer.txt)
* [jobs/inline_evolved_entertainer](common/inline_scripts/jobs/inline_evolved_entertainer.txt)
* [jobs/inline_evolved_executive_civic_swaps](common/inline_scripts/jobs/inline_evolved_executive_civic_swaps.txt)
* [jobs/inline_evolved_farmer](common/inline_scripts/jobs/inline_evolved_farmer.txt)
* [jobs/inline_evolved_farmer_secondary](common/inline_scripts/jobs/inline_evolved_farmer_secondary.txt)
* [jobs/inline_evolved_foundry](common/inline_scripts/jobs/inline_evolved_foundry.txt)
* [jobs/inline_evolved_healthcare](common/inline_scripts/jobs/inline_evolved_healthcare.txt)
* [jobs/inline_evolved_maintenance_civic_hive_swaps](common/inline_scripts/jobs/inline_evolved_maintenance_civic_hive_swaps.txt)
* [jobs/inline_evolved_maintenance_civic_machine_swaps](common/inline_scripts/jobs/inline_evolved_maintenance_civic_machine_swaps.txt)
* [jobs/inline_evolved_maintenance_drone](common/inline_scripts/jobs/inline_evolved_maintenance_drone.txt)
* [jobs/inline_evolved_miner](common/inline_scripts/jobs/inline_evolved_miner.txt)
* [jobs/inline_evolved_miner_secondary](common/inline_scripts/jobs/inline_evolved_miner_secondary.txt)
* [jobs/inline_evolved_patrol_drone](common/inline_scripts/jobs/inline_evolved_patrol_drone.txt)
* [jobs/inline_evolved_politician_civic_swaps](common/inline_scripts/jobs/inline_evolved_politician_civic_swaps.txt)
* [jobs/inline_evolved_priest](common/inline_scripts/jobs/inline_evolved_priest.txt)
* [jobs/inline_evolved_priest_swaps](common/inline_scripts/jobs/inline_evolved_priest_swaps.txt)
* [jobs/inline_evolved_prime_drone](common/inline_scripts/jobs/inline_evolved_prime_drone.txt)
* [jobs/inline_evolved_researcher](common/inline_scripts/jobs/inline_evolved_researcher.txt)
* [jobs/inline_evolved_researcher_swaps](common/inline_scripts/jobs/inline_evolved_researcher_swaps.txt)
* [jobs/inline_evolved_soldier](common/inline_scripts/jobs/inline_evolved_soldier.txt)
* [jobs/inline_evolved_synapse_civic_swaps](common/inline_scripts/jobs/inline_evolved_synapse_civic_swaps.txt)
* [jobs/inline_evolved_technician](common/inline_scripts/jobs/inline_evolved_technician.txt)
* [jobs/inline_evolved_technician_secondary](common/inline_scripts/jobs/inline_evolved_technician_secondary.txt)
* [jobs/inline_evolved_warrior_drone](common/inline_scripts/jobs/inline_evolved_warrior_drone.txt)
* [mod_support/inline_evolved_spiritualist_cults](common/inline_scripts/mod_support/inline_evolved_spiritualist_cults.txt)
* [modifiers/inline_evolved_artisan_efficiency](common/inline_scripts/modifiers/inline_evolved_artisan_efficiency.txt)
* [modifiers/inline_evolved_farmer_efficiency](common/inline_scripts/modifiers/inline_evolved_farmer_efficiency.txt)
* [modifiers/inline_evolved_foundry_efficiency](common/inline_scripts/modifiers/inline_evolved_foundry_efficiency.txt)
* [modifiers/inline_evolved_miner_efficiency](common/inline_scripts/modifiers/inline_evolved_miner_efficiency.txt)
* [modifiers/inline_evolved_rural_farming_district_build_speed](common/inline_scripts/modifiers/inline_evolved_rural_farming_district_build_speed.txt)
* [modifiers/inline_evolved_rural_farming_district_max](common/inline_scripts/modifiers/inline_evolved_rural_farming_district_max.txt)
* [modifiers/inline_evolved_rural_generator_district_build_speed](common/inline_scripts/modifiers/inline_evolved_rural_generator_district_build_speed.txt)
* [modifiers/inline_evolved_rural_generator_district_max](common/inline_scripts/modifiers/inline_evolved_rural_generator_district_max.txt)
* [modifiers/inline_evolved_rural_mining_district_build_speed](common/inline_scripts/modifiers/inline_evolved_rural_mining_district_build_speed.txt)
* [modifiers/inline_evolved_rural_mining_district_max](common/inline_scripts/modifiers/inline_evolved_rural_mining_district_max.txt)
* [modifiers/inline_evolved_technician_efficiency](common/inline_scripts/modifiers/inline_evolved_technician_efficiency.txt)
