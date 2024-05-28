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
