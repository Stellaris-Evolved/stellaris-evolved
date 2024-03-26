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

* [tec_has_artisan_upkeep_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L429)
* [tec_has_artisan_upkeep_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L420)
* [tec_has_bureaucratic_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L333)
* [tec_has_clerk_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L52)
* [tec_has_clinic_building_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L157)
* [tec_has_colonist_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L37)
* [tec_has_coordinator_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L67)
* [tec_has_cyborg_clinic_exception](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L172)
* [tec_has_diplomatic_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1148)
* [tec_has_directive_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L592)
* [tec_has_enforcer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L22)
* [tec_has_entertainer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L7)
* [tec_has_farmer_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L201)
* [tec_has_farmer_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L438)
* [tec_has_farmer_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L183)
* [tec_has_forced_living_standard_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L634)
* [tec_has_foundry_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L318)
* [tec_has_foundry_upkeep_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L411)
* [tec_has_foundry_upkeep_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L399)
* [tec_has_healthcare_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L141)
* [tec_has_maintenance_drone_swap_civic_hive](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L553)
* [tec_has_maintenance_drone_swap_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L618)
* [tec_has_maintenance_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L98)
* [tec_has_matter_miner](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L267)
* [tec_has_miner_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L234)
* [tec_has_miner_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L457)
* [tec_has_miner_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L217)
* [tec_has_monument_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L357)
* [tec_has_naval_academy_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L389)
* [tec_has_patrol_drone_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L112)
* [tec_has_research_lab_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L368)
* [tec_has_ruler_civic_hive](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L531)
* [tec_has_ruler_civic_machine](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L568)
* [tec_has_ruler_civic_mega](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L504)
* [tec_has_ruler_civic_regular](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L418)
* [tec_has_scrap_miner](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L469)
* [tec_has_slaver_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1126)
* [tec_has_soldier_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L82)
* [tec_has_special_ruler_feature](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L374)
* [tec_has_spy_civic](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L1139)
* [tec_has_stronghold_buildings_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L378)
* [tec_has_technician_planet_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L303)
* [tec_has_technician_production_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L478)
* [tec_has_technician_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L286)
* [tec_has_warrior_drone_swap](common/scripted_triggers/zzz_evolved_swaps_triggers.txt#L126)
* [tec_is_special_researcher_empire](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L161)
* [tec_is_spiritualist_main_cult](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L331)
* [tec_is_spiritualist_secondary_cult](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L351)
* [tec_replaces_half_researcher_empire](common/scripted_triggers/zzz_evolved_country_scripted_triggers.txt#L183)

## Current supported scripted_effects

* [tec_cache_building_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L192)
* [tec_cache_capital_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L154)
* [tec_cache_colony_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L231)
* [tec_cache_country_civic_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L421)
* [tec_cache_country_councilor_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L659)
* [tec_cache_country_monthly_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L353)
* [tec_cache_planet_type_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L39)
* [tec_cache_pop_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L287)
* [tec_cache_species_traits_triggers](common/scripted_effects/zz_evolved_scripted_effects.txt#L331)

## Current supported inline_scripts


