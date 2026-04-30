# VOICE_FIRST_LISTING_DIAGNOSTIC_V1

## Goal
Telegram bot must understand short voice/text commands about a specific listing and run a safe diagnostic.

## Example commands
- this listing does not work
- check listing 318222589463
- why no sales
- check views and watchers
- analyze performance
- compare with competitors
- improve title
- check photos
- check item specifics
- build dry improvement plan

## Input types
- listing ID
- SKU
- offer ID
- marketplace name
- product name
- pasted URL
- voice note
- short text command

## Flow
1. Transcribe voice or read text
2. Detect intent
3. Resolve listing identity
4. Detect marketplace profile: eBay, Amazon, Shopify, etc.
5. Read current listing data only
6. Read performance data where available
7. Run quality score
8. Run competitor comparison
9. Run critic
10. Return short operator result
11. If needed, build dry plan
12. Ask approve/reject before any live action

## Diagnostic output
- current status
- likely problem
- quality score
- performance signals
- missing data
- competitor gap
- recommended next step
- risk warning

## Safety
- Read-only by default
- No publish/revise/delete from voice command alone
- Live action needs explicit approval button or approval phrase

## Priority
NEXT after eBay Quality Foundation and basic performance dataset.
