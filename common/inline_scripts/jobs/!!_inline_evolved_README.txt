# This file is a README, doccumenting general structure of inlines
# for the purpose of standardization and reducing repetition.

# Below we will document general parameter names used in the inlines in this
# folder, with the prefix `inline_evolved_`

# trigger - allows passing a trigger when a job is added/description is displayed.
	# Some jobs have some innate conditions, the trigger in this cases being extra
	# restrictions, will be useful for PD arcologies and PW wonders since some jobs 
	# are not added if some conditions are not met. 

	# Also useful for capital for conditional hald swaps as seen in regular file.
# /

# count - amount of jobs that will given

# mult - mult value to pass to the triggered modifiers

# display - specify how the modifier is displayed, mainly if triggered description is added or not.
	# Valid values: `with_desc` and `no_desc`. When defaults are allowed, will default to `with_desc`
	# Temporary parameter till conditionals and defaults are available in inline_scripts
# /