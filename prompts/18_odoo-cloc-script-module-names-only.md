---
title: "Odoo cloc script module names only"
state: draft
model: 
input_tokens: 
---

# Run 18

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

The `roles/odoo/files/docker-odoo-cloc` command procues and output like this:

````bash
docker-odoo-cloc -c odoo04 -d donuteconomics
2026-08-05 10:51:07,718 366 INFO donuteconomics odoo.modules.loading: loading 1 modules...
2026-08-05 10:51:07,880 366 INFO donuteconomics odoo.addons.base.models.ir_actions_report: Will use the Wkhtmltopdf binary at /usr/local/bin/wkhtmltopdf
2026-08-05 10:51:08,317 366 INFO donuteconomics odoo.modules.loading: 1 modules loaded in 0.60s, 0 queries (+0 extra)
2026-08-05 10:51:08,382 366 INFO donuteconomics odoo.modules.loading: loading 121 modules...
2026-08-05 10:51:09,057 366 WARNING donuteconomics odoo.api.create: The model odoo.addons.subscription_oca.models.sale_subscription is not overriding the create method in batch
2026-08-05 10:51:09,067 366 INFO donuteconomics odoo.modules.loading: 121 modules loaded in 0.68s, 0 queries (+0 extra)
2026-08-05 10:51:09,220 366 INFO donuteconomics odoo.modules.loading: Modules loaded.
2026-08-05 10:51:09,228 366 INFO donuteconomics odoo.modules.registry: Registry loaded in 1.528s
Odoo cloc                                                                                                                      Line   Other    Code
---------------------------------------------------------------------------------------------------------------------------------------------------
account_financial_report                                                                                                      11422    2022    9400
account_reconcile_oca                                                                                                          3046     433    2613
account_statement_base                                                                                                          415      49     366
account_statement_import_base                                                                                                   124      49      75
account_statement_import_camt                                                                                                   580     147     433
account_statement_import_camt54                                                                                                 187      61     126
account_statement_import_file                                                                                                   532     177     355
account_usability                                                                                                               549     119     430
auth_impersonate_user                                                                                                           143      40     103
contract                                                                                                                       6048     993    5055
contract_sale                                                                                                                   115       4     111
contract_sale_generation                                                                                                        297      87     210
date_range                                                                                                                     1127     198     929
helpdesk_mgmt                                                                                                                  3178     277    2901
mass_mailing_list_dynamic                                                                                                       290      84     206
mass_mailing_partner                                                                                                            677     175     502
mis_builder                                                                                                                    6153    1734    4419
mis_template_financial_report                                                                                                   327      27     300
odoo/studio                                                                                                                      71      31      40
partner_deduplicate_acl                                                                                                         112      31      81
partner_firstname                                                                                                               574     166     408
prometheus_exporter                                                                                                             229      43     186
report_xlsx                                                                                                                     380     125     255
subscription_oca                                                                                                               2041     351    1690
web_responsive                                                                                                                 2520     358    2162
---------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                              41137    7781   33356
````

I would like to have an option `-s` for short. If applied to the standard output contains only the module names:

```
account_financial_report
account_reconcile_oca
account_statement_base
...
````

The `odoo/studio` is removed.


## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker Set frontmatter state to completed and update info about model and token usage.
