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

Scripted triggers that have the `tec_trigger_mod_support`, and scripted effects that have the `tec_effect_mod_support`
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

## Current supported scripted_triggers

* [tec_blocks_industrial_designations](common\scripted_triggers\zzz_evolved_scripted_triggers.txt#L4559)
* [tec_blocks_non_industrial_designations](common\scripted_triggers\zzz_evolved_scripted_triggers.txt#L4573)
* [tec_blocks_regular_designations](common\scripted_triggers\zzz_evolved_scripted_triggers.txt#L4519)
* [tec_blocks_rural_designations](common\scripted_triggers\zzz_evolved_scripted_triggers.txt#L4546)
* [tec_blocks_urban_designations](common\scripted_triggers\zzz_evolved_scripted_triggers.txt#L4531)
* [tec_country_has_autocratic_authority](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L1792)
* [tec_country_has_democratic_authority](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L1772)
* [tec_country_has_oligarchic_authority](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L1782)
* [tec_has_artisan_upkeep_planet_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L429)
* [tec_has_artisan_upkeep_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L420)
* [tec_has_bureaucratic_buildings_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L333)
* [tec_has_clerk_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L52)
* [tec_has_clinic_building_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L157)
* [tec_has_colonist_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L37)
* [tec_has_coordinator_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L67)
* [tec_has_cyborg_clinic_exception](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L172)
* [tec_has_diplomatic_civic](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L1156)
* [tec_has_directive_civic_machine](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L594)
* [tec_has_enforcer_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L22)
* [tec_has_entertainer_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L7)
* [tec_has_farmer_planet_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L201)
* [tec_has_farmer_production_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L438)
* [tec_has_farmer_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L183)
* [tec_has_forced_living_standard_civic](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L636)
* [tec_has_foundry_planet_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L318)
* [tec_has_foundry_upkeep_planet_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L411)
* [tec_has_foundry_upkeep_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L399)
* [tec_has_healthcare_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L141)
* [tec_has_maintenance_drone_swap_civic_hive](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L555)
* [tec_has_maintenance_drone_swap_civic_machine](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L620)
* [tec_has_maintenance_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L98)
* [tec_has_matter_miner](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L267)
* [tec_has_miner_planet_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L234)
* [tec_has_miner_production_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L457)
* [tec_has_miner_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L217)
* [tec_has_monument_buildings_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L357)
* [tec_has_naval_academy_buildings_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L389)
* [tec_has_patrol_drone_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L112)
* [tec_has_research_lab_buildings_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L368)
* [tec_has_ruler_civic_hive](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L533)
* [tec_has_ruler_civic_machine](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L570)
* [tec_has_ruler_civic_mega](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L506)
* [tec_has_ruler_civic_regular](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L420)
* [tec_has_scrap_miner](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L469)
* [tec_has_slaver_civic](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L1134)
* [tec_has_soldier_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L82)
* [tec_has_special_ruler_feature](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L376)
* [tec_has_spy_civic](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L1147)
* [tec_has_stronghold_buildings_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L378)
* [tec_has_technician_planet_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L303)
* [tec_has_technician_production_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L478)
* [tec_has_technician_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L286)
* [tec_has_warrior_drone_swap](common\scripted_triggers\zzz_evolved_swaps_triggers.txt#L126)
* [tec_is_special_researcher_empire](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L161)
* [tec_is_spiritualist_main_cult](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L331)
* [tec_is_spiritualist_secondary_cult](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L353)
* [tec_replaces_half_researcher_empire](common\scripted_triggers\zzz_evolved_country_scripted_triggers.txt#L183)

## Current supported scripted_effects

* [tec_cache_building_triggers](common\scripted_effects\zz_evolved_scripted_effects.txt#L196)
* [tec_cache_capital_triggers](common\scripted_effects\zz_evolved_scripted_effects.txt#L158)
* [tec_cache_colony_triggers](common\scripted_effects\zz_evolved_scripted_effects.txt#L235)
* [tec_cache_combined_values](common\scripted_effects\zz_evolved_scripted_effects.txt#L203)
* [tec_cache_country_civic_triggers](common\scripted_effects\zz_evolved_scripted_effects.txt#L483)
* [tec_cache_country_monthly_triggers](common\scripted_effects\zz_evolved_scripted_effects.txt#L415)
* [tec_cache_planet_type_triggers](common\scripted_effects\zz_evolved_scripted_effects.txt#L43)
* [tec_cache_pop_triggers](common\scripted_effects\zz_evolved_scripted_effects.txt#L310)
* [tec_cache_species_traits_triggers](common\scripted_effects\zz_evolved_scripted_effects.txt#L393)

## Current supported inline_scripts

* [buildings/convert_to/tec_assembly_bioservant_1](common\inline_scripts\buildings\convert_to\tec_assembly_bioservant_1.txt)
* [buildings/convert_to/tec_assembly_bioservant_2](common\inline_scripts\buildings\convert_to\tec_assembly_bioservant_2.txt)
* [buildings/convert_to/tec_assembly_bioservant_3](common\inline_scripts\buildings\convert_to\tec_assembly_bioservant_3.txt)
* [buildings/convert_to/tec_assembly_organic_1](common\inline_scripts\buildings\convert_to\tec_assembly_organic_1.txt)
* [buildings/convert_to/tec_assembly_organic_2](common\inline_scripts\buildings\convert_to\tec_assembly_organic_2.txt)
* [buildings/convert_to/tec_assembly_organic_3](common\inline_scripts\buildings\convert_to\tec_assembly_organic_3.txt)
* [buildings/convert_to/tec_assembly_robotic_1](common\inline_scripts\buildings\convert_to\tec_assembly_robotic_1.txt)
* [buildings/convert_to/tec_assembly_robotic_2](common\inline_scripts\buildings\convert_to\tec_assembly_robotic_2.txt)
* [buildings/convert_to/tec_assembly_robotic_3](common\inline_scripts\buildings\convert_to\tec_assembly_robotic_3.txt)
* [buildings/convert_to/tec_bureaucratic_1](common\inline_scripts\buildings\convert_to\tec_bureaucratic_1.txt)
* [buildings/convert_to/tec_bureaucratic_2](common\inline_scripts\buildings\convert_to\tec_bureaucratic_2.txt)
* [buildings/convert_to/tec_bureaucratic_3](common\inline_scripts\buildings\convert_to\tec_bureaucratic_3.txt)
* [buildings/convert_to/tec_capital_t1](common\inline_scripts\buildings\convert_to\tec_capital_t1.txt)
* [buildings/convert_to/tec_capital_t2](common\inline_scripts\buildings\convert_to\tec_capital_t2.txt)
* [buildings/convert_to/tec_capital_t3](common\inline_scripts\buildings\convert_to\tec_capital_t3.txt)
* [buildings/convert_to/tec_capital_t4](common\inline_scripts\buildings\convert_to\tec_capital_t4.txt)
* [buildings/convert_to/tec_capital_t5](common\inline_scripts\buildings\convert_to\tec_capital_t5.txt)
* [buildings/convert_to/tec_clinic_1](common\inline_scripts\buildings\convert_to\tec_clinic_1.txt)
* [buildings/convert_to/tec_clinic_2](common\inline_scripts\buildings\convert_to\tec_clinic_2.txt)
* [buildings/convert_to/tec_clinic_3](common\inline_scripts\buildings\convert_to\tec_clinic_3.txt)
* [buildings/convert_to/tec_housing_1](common\inline_scripts\buildings\convert_to\tec_housing_1.txt)
* [buildings/convert_to/tec_housing_2](common\inline_scripts\buildings\convert_to\tec_housing_2.txt)
* [buildings/convert_to/tec_monument_1](common\inline_scripts\buildings\convert_to\tec_monument_1.txt)
* [buildings/convert_to/tec_monument_2](common\inline_scripts\buildings\convert_to\tec_monument_2.txt)
* [buildings/convert_to/tec_monument_3](common\inline_scripts\buildings\convert_to\tec_monument_3.txt)
* [buildings/convert_to/tec_naval_academy_1](common\inline_scripts\buildings\convert_to\tec_naval_academy_1.txt)
* [buildings/convert_to/tec_naval_academy_2](common\inline_scripts\buildings\convert_to\tec_naval_academy_2.txt)
* [buildings/convert_to/tec_naval_academy_3](common\inline_scripts\buildings\convert_to\tec_naval_academy_3.txt)
* [buildings/convert_to/tec_research_1](common\inline_scripts\buildings\convert_to\tec_research_1.txt)
* [buildings/convert_to/tec_research_2](common\inline_scripts\buildings\convert_to\tec_research_2.txt)
* [buildings/convert_to/tec_research_3](common\inline_scripts\buildings\convert_to\tec_research_3.txt)
* [buildings/convert_to/tec_stronghold_1](common\inline_scripts\buildings\convert_to\tec_stronghold_1.txt)
* [buildings/convert_to/tec_stronghold_2](common\inline_scripts\buildings\convert_to\tec_stronghold_2.txt)
* [buildings/convert_to/tec_stronghold_3](common\inline_scripts\buildings\convert_to\tec_stronghold_3.txt)
* [buildings/convert_to/tec_temple_1](common\inline_scripts\buildings\convert_to\tec_temple_1.txt)
* [buildings/convert_to/tec_temple_2](common\inline_scripts\buildings\convert_to\tec_temple_2.txt)
* [buildings/convert_to/tec_temple_3](common\inline_scripts\buildings\convert_to\tec_temple_3.txt)
* [buildings/effects/type/tec_bureaucratic](common\inline_scripts\buildings\effects\type\tec_bureaucratic.txt)
* [buildings/effects/type/tec_bureaucratic_hive](common\inline_scripts\buildings\effects\type\tec_bureaucratic_hive.txt)
* [buildings/effects/type/tec_bureaucratic_machine](common\inline_scripts\buildings\effects\type\tec_bureaucratic_machine.txt)
* [buildings/effects/type/tec_bureaucratic_regular](common\inline_scripts\buildings\effects\type\tec_bureaucratic_regular.txt)
* [buildings/effects/type/tec_chemical_plant](common\inline_scripts\buildings\effects\type\tec_chemical_plant.txt)
* [buildings/effects/type/tec_crystal_plant](common\inline_scripts\buildings\effects\type\tec_crystal_plant.txt)
* [buildings/effects/type/tec_energrid](common\inline_scripts\buildings\effects\type\tec_energrid.txt)
* [buildings/effects/type/tec_energy_grid](common\inline_scripts\buildings\effects\type\tec_energy_grid.txt)
* [buildings/effects/type/tec_factory](common\inline_scripts\buildings\effects\type\tec_factory.txt)
* [buildings/effects/type/tec_food_processing_facility](common\inline_scripts\buildings\effects\type\tec_food_processing_facility.txt)
* [buildings/effects/type/tec_fortress](common\inline_scripts\buildings\effects\type\tec_fortress.txt)
* [buildings/effects/type/tec_fortress_hive](common\inline_scripts\buildings\effects\type\tec_fortress_hive.txt)
* [buildings/effects/type/tec_fortress_machine](common\inline_scripts\buildings\effects\type\tec_fortress_machine.txt)
* [buildings/effects/type/tec_fortress_regular](common\inline_scripts\buildings\effects\type\tec_fortress_regular.txt)
* [buildings/effects/type/tec_foundry](common\inline_scripts\buildings\effects\type\tec_foundry.txt)
* [buildings/effects/type/tec_healthcare](common\inline_scripts\buildings\effects\type\tec_healthcare.txt)
* [buildings/effects/type/tec_hydroponics_farm](common\inline_scripts\buildings\effects\type\tec_hydroponics_farm.txt)
* [buildings/effects/type/tec_military_booster](common\inline_scripts\buildings\effects\type\tec_military_booster.txt)
* [buildings/effects/type/tec_mineral_purification_plant](common\inline_scripts\buildings\effects\type\tec_mineral_purification_plant.txt)
* [buildings/effects/type/tec_ministry_production](common\inline_scripts\buildings\effects\type\tec_ministry_production.txt)
* [buildings/effects/type/tec_monument](common\inline_scripts\buildings\effects\type\tec_monument.txt)
* [buildings/effects/type/tec_monument_hive](common\inline_scripts\buildings\effects\type\tec_monument_hive.txt)
* [buildings/effects/type/tec_monument_machine](common\inline_scripts\buildings\effects\type\tec_monument_machine.txt)
* [buildings/effects/type/tec_monument_regular](common\inline_scripts\buildings\effects\type\tec_monument_regular.txt)
* [buildings/effects/type/tec_naval_academy](common\inline_scripts\buildings\effects\type\tec_naval_academy.txt)
* [buildings/effects/type/tec_naval_academy_hive](common\inline_scripts\buildings\effects\type\tec_naval_academy_hive.txt)
* [buildings/effects/type/tec_naval_academy_machine](common\inline_scripts\buildings\effects\type\tec_naval_academy_machine.txt)
* [buildings/effects/type/tec_naval_academy_regular](common\inline_scripts\buildings\effects\type\tec_naval_academy_regular.txt)
* [buildings/effects/type/tec_refinery](common\inline_scripts\buildings\effects\type\tec_refinery.txt)
* [buildings/effects/type/tec_research_lab](common\inline_scripts\buildings\effects\type\tec_research_lab.txt)
* [buildings/effects/type/tec_research_lab_hive](common\inline_scripts\buildings\effects\type\tec_research_lab_hive.txt)
* [buildings/effects/type/tec_research_lab_machine](common\inline_scripts\buildings\effects\type\tec_research_lab_machine.txt)
* [buildings/effects/type/tec_research_lab_regular](common\inline_scripts\buildings\effects\type\tec_research_lab_regular.txt)
* [buildings/effects/type/tec_resource_silo](common\inline_scripts\buildings\effects\type\tec_resource_silo.txt)
* [buildings/effects/type/tec_robot_assembly](common\inline_scripts\buildings\effects\type\tec_robot_assembly.txt)
* [buildings/effects/type/tec_robot_assembly_hive](common\inline_scripts\buildings\effects\type\tec_robot_assembly_hive.txt)
* [buildings/effects/type/tec_robot_assembly_machine](common\inline_scripts\buildings\effects\type\tec_robot_assembly_machine.txt)
* [buildings/effects/type/tec_robot_assembly_regular](common\inline_scripts\buildings\effects\type\tec_robot_assembly_regular.txt)
* [buildings/effects/type/tec_stripmine](common\inline_scripts\buildings\effects\type\tec_stripmine.txt)
* [buildings/effects/type/tec_temple](common\inline_scripts\buildings\effects\type\tec_temple.txt)
* [buildings/effects/type/tec_trade](common\inline_scripts\buildings\effects\type\tec_trade.txt)
* [buildings/effects/type/tec_trade_hive](common\inline_scripts\buildings\effects\type\tec_trade_hive.txt)
* [buildings/effects/type/tec_trade_machine](common\inline_scripts\buildings\effects\type\tec_trade_machine.txt)
* [buildings/effects/type/tec_trade_regular](common\inline_scripts\buildings\effects\type\tec_trade_regular.txt)
* [capitals/tec_all_capital](common\inline_scripts\capitals\tec_all_capital.txt)
* [capitals/tec_colony](common\inline_scripts\capitals\tec_colony.txt)
* [capitals/tec_colony_habitat](common\inline_scripts\capitals\tec_colony_habitat.txt)
* [capitals/tec_common_habitat_modifiers](common\inline_scripts\capitals\tec_common_habitat_modifiers.txt)
* [capitals/tec_common_modifiers](common\inline_scripts\capitals\tec_common_modifiers.txt)
* [capitals/tec_hive_capital](common\inline_scripts\capitals\tec_hive_capital.txt)
* [capitals/tec_machine_capital](common\inline_scripts\capitals\tec_machine_capital.txt)
* [capitals/tec_regular_capital](common\inline_scripts\capitals\tec_regular_capital.txt)
* [capitals/tec_special_capital](common\inline_scripts\capitals\tec_special_capital.txt)
* [districts/type/tec_housing_arcology](common\inline_scripts\districts\type\tec_housing_arcology.txt)
* [districts/type/tec_housing_city](common\inline_scripts\districts\type\tec_housing_city.txt)
* [districts/type/tec_housing_generic](common\inline_scripts\districts\type\tec_housing_generic.txt)
* [districts/type/tec_housing_habitat](common\inline_scripts\districts\type\tec_housing_habitat.txt)
* [districts/type/tec_housing_hive](common\inline_scripts\districts\type\tec_housing_hive.txt)
* [districts/type/tec_housing_nexus](common\inline_scripts\districts\type\tec_housing_nexus.txt)
* [districts/type/tec_maintenance](common\inline_scripts\districts\type\tec_maintenance.txt)
* [districts/type/tec_research](common\inline_scripts\districts\type\tec_research.txt)
* [districts/type/tec_rural_farming](common\inline_scripts\districts\type\tec_rural_farming.txt)
* [districts/type/tec_rural_generator](common\inline_scripts\districts\type\tec_rural_generator.txt)
* [districts/type/tec_rural_mining](common\inline_scripts\districts\type\tec_rural_mining.txt)
* [districts/type/tec_trade](common\inline_scripts\districts\type\tec_trade.txt)
* [districts/type/tec_unity](common\inline_scripts\districts\type\tec_unity.txt)
* [jobs/capital/tec_add_job_civic_hive](common\inline_scripts\jobs\capital\tec_add_job_civic_hive.txt)
* [jobs/capital/tec_add_job_civic_machine](common\inline_scripts\jobs\capital\tec_add_job_civic_machine.txt)
* [jobs/capital/tec_add_job_civic_regular](common\inline_scripts\jobs\capital\tec_add_job_civic_regular.txt)
* [jobs/capital/tec_add_job_per_ascension_civic_hive](common\inline_scripts\jobs\capital\tec_add_job_per_ascension_civic_hive.txt)
* [jobs/capital/tec_add_job_per_ascension_civic_machine](common\inline_scripts\jobs\capital\tec_add_job_per_ascension_civic_machine.txt)
* [jobs/capital/tec_add_job_per_ascension_civic_regular](common\inline_scripts\jobs\capital\tec_add_job_per_ascension_civic_regular.txt)
* [jobs/capital/tec_add_ruler_civic_regular](common\inline_scripts\jobs\capital\tec_add_ruler_civic_regular.txt)
* [jobs/tec_clerk](common\inline_scripts\jobs\tec_clerk.txt)
* [jobs/tec_colonist](common\inline_scripts\jobs\tec_colonist.txt)
* [jobs/tec_coordinator](common\inline_scripts\jobs\tec_coordinator.txt)
* [jobs/tec_enforcer](common\inline_scripts\jobs\tec_enforcer.txt)
* [jobs/tec_entertainer](common\inline_scripts\jobs\tec_entertainer.txt)
* [jobs/tec_executive_civic_swaps](common\inline_scripts\jobs\tec_executive_civic_swaps.txt)
* [jobs/tec_farmer](common\inline_scripts\jobs\tec_farmer.txt)
* [jobs/tec_farmer_secondary](common\inline_scripts\jobs\tec_farmer_secondary.txt)
* [jobs/tec_foundry](common\inline_scripts\jobs\tec_foundry.txt)
* [jobs/tec_healthcare](common\inline_scripts\jobs\tec_healthcare.txt)
* [jobs/tec_maintenance_civic_hive_swaps](common\inline_scripts\jobs\tec_maintenance_civic_hive_swaps.txt)
* [jobs/tec_maintenance_civic_machine_swaps](common\inline_scripts\jobs\tec_maintenance_civic_machine_swaps.txt)
* [jobs/tec_maintenance_drone](common\inline_scripts\jobs\tec_maintenance_drone.txt)
* [jobs/tec_miner](common\inline_scripts\jobs\tec_miner.txt)
* [jobs/tec_miner_secondary](common\inline_scripts\jobs\tec_miner_secondary.txt)
* [jobs/tec_patrol_drone](common\inline_scripts\jobs\tec_patrol_drone.txt)
* [jobs/tec_politician_civic_swaps](common\inline_scripts\jobs\tec_politician_civic_swaps.txt)
* [jobs/tec_priest](common\inline_scripts\jobs\tec_priest.txt)
* [jobs/tec_priest_swaps](common\inline_scripts\jobs\tec_priest_swaps.txt)
* [jobs/tec_prime_drone](common\inline_scripts\jobs\tec_prime_drone.txt)
* [jobs/tec_researcher](common\inline_scripts\jobs\tec_researcher.txt)
* [jobs/tec_researcher_swaps](common\inline_scripts\jobs\tec_researcher_swaps.txt)
* [jobs/tec_soldier](common\inline_scripts\jobs\tec_soldier.txt)
* [jobs/tec_spawning_drone](common\inline_scripts\jobs\tec_spawning_drone.txt)
* [jobs/tec_synapse_civic_swaps](common\inline_scripts\jobs\tec_synapse_civic_swaps.txt)
* [jobs/tec_technician](common\inline_scripts\jobs\tec_technician.txt)
* [jobs/tec_technician_secondary](common\inline_scripts\jobs\tec_technician_secondary.txt)
* [jobs/tec_warrior_drone](common\inline_scripts\jobs\tec_warrior_drone.txt)
* [mod_support/tec_$authority$_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_corporate_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_democratic_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_dictatorial_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_direct_democratic_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_hive_mind_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_imperial_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_machine_intelligence_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_oligarchic_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_tec_ai_corporate_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_tec_ai_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_tec_hive_biological_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_tec_hive_biomechanical_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_tec_hive_cybernetic_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_tec_machine_consensus_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_tec_patrocorporate_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_auth_tec_theocracy_swaps](common\inline_scripts\mod_support\tec_auth_swaps.txt)
* [mod_support/tec_spiritualist_cults](common\inline_scripts\mod_support\tec_spiritualist_cults.txt)
* [modifiers/tec_artisan_efficiency](common\inline_scripts\modifiers\tec_artisan_efficiency.txt)
* [modifiers/tec_farmer_efficiency](common\inline_scripts\modifiers\tec_farmer_efficiency.txt)
* [modifiers/tec_foundry_efficiency](common\inline_scripts\modifiers\tec_foundry_efficiency.txt)
* [modifiers/tec_miner_efficiency](common\inline_scripts\modifiers\tec_miner_efficiency.txt)
* [modifiers/tec_rural_farming_district_build_speed](common\inline_scripts\modifiers\tec_rural_farming_district_build_speed.txt)
* [modifiers/tec_rural_farming_district_max](common\inline_scripts\modifiers\tec_rural_farming_district_max.txt)
* [modifiers/tec_rural_generator_district_build_speed](common\inline_scripts\modifiers\tec_rural_generator_district_build_speed.txt)
* [modifiers/tec_rural_generator_district_max](common\inline_scripts\modifiers\tec_rural_generator_district_max.txt)
* [modifiers/tec_rural_mining_district_build_speed](common\inline_scripts\modifiers\tec_rural_mining_district_build_speed.txt)
* [modifiers/tec_rural_mining_district_max](common\inline_scripts\modifiers\tec_rural_mining_district_max.txt)
* [modifiers/tec_technician_efficiency](common\inline_scripts\modifiers\tec_technician_efficiency.txt)
