# CompanyVendorSyncBodyUpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**address** | **str** | Address | [optional] 
**city** | **str** | City | [optional] 
**zip** | **str** | Zip code | [optional] 
**business_phone** | **str** | Business phone | [optional] 
**mobile_phone** | **str** | Mobile phone | [optional] 
**fax_number** | **str** | Fax number | [optional] 
**email_address** | **str** | Email address | [optional] 
**is_active** | **bool** | Active status | [optional] 
**state_code** | **str** | State code (ISO-3166 Alpha-2 format) | [optional] 
**authorized_bidder** | **bool** | Authorized bidder status | [optional] 
**prequalified** | **bool** | Prequalified status | [optional] [default to False]
**country_code** | **str** | Country code (ISO-3166 Alpha-2 format) | [optional] 
**labor_union** | **str** | Labor union | [optional] 
**license_number** | **str** | License number | [optional] 
**website** | **str** | Website url | [optional] 
**union_member** | **bool** | Union member status | [optional] 
**non_union_prevailing_wage** | **bool** | Non union prevailing wage status | [optional] 
**abbreviated_name** | **str** | Abbreviated name | [optional] 
**notes** | **str** | Notes (notes/keywords/tags) | [optional] 
**vendor_group_id** | **int** | Vendor Group ID | [optional] 
**parent_id** | **int** | Parent Vendor ID. Cannot be the same as ID. Only two levels of hierarchy are supported (parent/child). | [optional] 
**primary_contact_id** | **int** | Primary Contact ID | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_code** | **str** | Origin Code | [optional] 
**trade_ids** | **List[int]** |  | [optional] 
**bidding_distribution_ids** | **List[int]** |  | [optional] 
**standard_cost_code_ids** | **List[int]** |  | [optional] 
**trade_name** | **str** | Vendor&#39;s Trade Name, also known as Doing Business As (DBA). | [optional] 
**bidding** | [**CompanyVendorSyncBodyUpdatesInnerBidding**](CompanyVendorSyncBodyUpdatesInnerBidding.md) |  | [optional] 

## Example

```python
from procore_sdk.models.company_vendor_sync_body_updates_inner import CompanyVendorSyncBodyUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyVendorSyncBodyUpdatesInner from a JSON string
company_vendor_sync_body_updates_inner_instance = CompanyVendorSyncBodyUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(CompanyVendorSyncBodyUpdatesInner.to_json())

# convert the object into a dict
company_vendor_sync_body_updates_inner_dict = company_vendor_sync_body_updates_inner_instance.to_dict()
# create an instance of CompanyVendorSyncBodyUpdatesInner from a dict
company_vendor_sync_body_updates_inner_from_dict = CompanyVendorSyncBodyUpdatesInner.from_dict(company_vendor_sync_body_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


