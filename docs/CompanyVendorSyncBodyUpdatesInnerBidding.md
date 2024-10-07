# CompanyVendorSyncBodyUpdatesInnerBidding

Bidding statuses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affirmative_action** | **bool** |  | [optional] [default to False]
**small_business** | **bool** |  | [optional] [default to False]
**african_american_business** | **bool** |  | [optional] [default to False]
**hispanic_business** | **bool** |  | [optional] [default to False]
**womens_business** | **bool** |  | [optional] [default to False]
**historically_underutilized_business** | **bool** |  | [optional] [default to False]
**sdvo_business** | **bool** |  | [optional] [default to False]
**certified_business_enterprise** | **bool** |  | [optional] [default to False]
**asian_american_business** | **bool** |  | [optional] [default to False]
**native_american_business** | **bool** |  | [optional] [default to False]
**disadvantaged_business** | **bool** |  | [optional] [default to False]
**minority_business_enterprise** | **bool** |  | [optional] [default to False]
**eight_a_business** | **bool** |  | [optional] [default to False]

## Example

```python
from procore_sdk.models.company_vendor_sync_body_updates_inner_bidding import CompanyVendorSyncBodyUpdatesInnerBidding

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyVendorSyncBodyUpdatesInnerBidding from a JSON string
company_vendor_sync_body_updates_inner_bidding_instance = CompanyVendorSyncBodyUpdatesInnerBidding.from_json(json)
# print the JSON string representation of the object
print(CompanyVendorSyncBodyUpdatesInnerBidding.to_json())

# convert the object into a dict
company_vendor_sync_body_updates_inner_bidding_dict = company_vendor_sync_body_updates_inner_bidding_instance.to_dict()
# create an instance of CompanyVendorSyncBodyUpdatesInnerBidding from a dict
company_vendor_sync_body_updates_inner_bidding_from_dict = CompanyVendorSyncBodyUpdatesInnerBidding.from_dict(company_vendor_sync_body_updates_inner_bidding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


