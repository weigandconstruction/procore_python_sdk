# RestV10VendorsGet200ResponseInner

Vendor Extended View

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**abbreviated_name** | **str** | Abbreviated name | [optional] 
**address** | **str** | Address | [optional] 
**attachments** | [**List[NormalViewAttachmentsInner]**](NormalViewAttachmentsInner.md) | Attachments | [optional] 
**authorized_bidder** | **bool** | Authorized bidder status | [optional] 
**business_id** | **str** | Business id | [optional] 
**business_phone** | **str** | Business phone | [optional] 
**business_register** | [**NormalViewBusinessRegister**](NormalViewBusinessRegister.md) |  | [optional] 
**city** | **str** | City | [optional] 
**contact_count** | **int** | Count of active Contacts associated with the vendor record. | [optional] 
**company** | **str** | Company | [optional] 
**country_code** | **str** | Country code (ISO-3166 Alpha-2 format) | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**email_address** | **str** | Email address | [optional] 
**fax_number** | **str** | Fax number | [optional] 
**is_active** | **bool** | Active status | [optional] 
**is_connected** | **bool** | Connected status | [optional] 
**labor_union** | **str** | Labor union | [optional] 
**license_number** | **str** | License number | [optional] 
**logo** | **str** | Logo url | [optional] 
**mobile_phone** | **str** | Mobile phone | [optional] 
**non_union_prevailing_wage** | **bool** | Non union prevailing wage status | [optional] 
**notes** | **str** | Notes | [optional] 
**origin_code** | **str** | Origin Code | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**prequalified** | **bool** | Prequalified status | [optional] 
**primary_contact** | [**NormalViewPrimaryContact**](NormalViewPrimaryContact.md) |  | [optional] 
**state_code** | **str** | State code (ISO-3166 Alpha-2 format) | [optional] 
**synced_to_erp** | **bool** | Synced to ERP | [optional] 
**trade_name** | **str** | Vendor&#39;s Trade Name, also known as Doing Business As (DBA). | [optional] 
**union_member** | **bool** | Union member status | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**vendor_group** | [**NormalViewVendorGroup**](NormalViewVendorGroup.md) |  | [optional] 
**website** | **str** | Website url | [optional] 
**zip** | **str** | Zip code | [optional] 
**bidding** | [**ExtendedView2Bidding**](ExtendedView2Bidding.md) |  | [optional] 
**bidding_distribution** | [**List[RestV10VendorsGet200ResponseInnerAllOfBiddingDistributionInner]**](RestV10VendorsGet200ResponseInnerAllOfBiddingDistributionInner.md) | Bidding distribution list | [optional] 
**children_count** | **int** | Count of vendors whose parent_id is this vendor&#39;s unique identifier | [optional] 
**company_vendor** | **bool** | Denotes whether this is the Company&#39;s Vendor | [optional] 
**legal_name** | **str** |  | [optional] 
**parent** | [**ExtendedView2Parent**](ExtendedView2Parent.md) |  | [optional] 
**project_ids** | **List[int]** | Array of Project IDs | [optional] 
**standard_cost_codes** | [**List[StandardCostCode]**](StandardCostCode.md) |  | [optional] 
**trades** | [**List[Trade2]**](Trade2.md) | Trades | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_vendors_get200_response_inner import RestV10VendorsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10VendorsGet200ResponseInner from a JSON string
rest_v10_vendors_get200_response_inner_instance = RestV10VendorsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10VendorsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_vendors_get200_response_inner_dict = rest_v10_vendors_get200_response_inner_instance.to_dict()
# create an instance of RestV10VendorsGet200ResponseInner from a dict
rest_v10_vendors_get200_response_inner_from_dict = RestV10VendorsGet200ResponseInner.from_dict(rest_v10_vendors_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


