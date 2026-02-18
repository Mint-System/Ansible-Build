---
title: The list-hosts command also shows hosting provider
---

# Run 06

Replace the `==` marked instructions in this file while you work on the task.

## Context

Read the `AGENTS.md` and `README.md` to get understanding of the project.

## Task

The `task lists-hosts` command should also show the Provider (`hosting_provider`) in the output table.

Update the command function.

## Worklog

1. Analyzed the current `list-hosts` function in the `task` file
2. Identified that the function has two branches: one for inventories with customer info and one without
3. Modified both branches to extract and display the `hosting_provider` field
4. Increased the customer column width from 35 to 55 to accommodate longer customer names
5. Fixed the issue with the `read` command splitting customer names on spaces by setting IFS=$'\t'
6. Tested the updated function with both types of inventories

## Summary

Successfully updated the `list-hosts` command to display the hosting provider information in the output table. The function now shows four columns: Alias, Host, Customer, and Provider for inventories with customer information, and three columns: Alias, Host, and Provider for inventories without customer information. The changes ensure proper formatting and handle special characters correctly.
