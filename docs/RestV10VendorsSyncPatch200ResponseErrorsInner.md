# RestV10VendorsSyncPatch200ResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**abbreviated_name** | **str** | Abbreviated name | [optional] 
**address** | **str** | Address | [optional] 
**authorized_bidder** | **bool** | Authorized bidder status | [optional] 
**business_phone** | **str** | Business phone | [optional] 
**city** | **str** | City | [optional] 
**contact_count** | **int** | Count of active Contacts associated with the vendor record | [optional] 
**company** | **str** | Company | [optional] 
**country_code** | **str** | Country code (ISO-3166 Alpha-2 format) | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**email_address** | **str** | Email address | [optional] 
**fax_number** | **str** | Fax number | [optional] 
**is_active** | **bool** | Active status | [optional] 
**labor_union** | **str** | Labor union | [optional] 
**license_number** | **str** | License number | [optional] 
**logo** | **str** | Logo url | [optional] 
**mobile_phone** | **str** | Mobile phone | [optional] 
**non_union_prevailing_wage** | **bool** | Non union prevailing wage status | [optional] 
**notes** | **str** | Notes | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**origin_code** | **str** | Origin Code | [optional] 
**prequalified** | **bool** | Prequalified status | [optional] 
**state_code** | **str** | State code (ISO-3166 Alpha-2 format) | [optional] 
**synced_to_erp** | **bool** | Synced to ERP | [optional] 
**trade_name** | **str** | Vendor&#39;s Trade Name, also known as Doing Business As (DBA). | [optional] 
**union_member** | **bool** | Union member status | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**website** | **str** | Website url | [optional] 
**zip** | **str** | Zip code | [optional] 
**business_register** | [**NormalViewBusinessRegister**](NormalViewBusinessRegister.md) |  | [optional] 
**vendor_group** | [**NormalViewVendorGroup**](NormalViewVendorGroup.md) |  | [optional] 
**primary_contact** | [**NormalViewPrimaryContact**](NormalViewPrimaryContact.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_vendors_sync_patch200_response_errors_inner import RestV10VendorsSyncPatch200ResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10VendorsSyncPatch200ResponseErrorsInner from a JSON string
rest_v10_vendors_sync_patch200_response_errors_inner_instance = RestV10VendorsSyncPatch200ResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10VendorsSyncPatch200ResponseErrorsInner.to_json())

# convert the object into a dict
rest_v10_vendors_sync_patch200_response_errors_inner_dict = rest_v10_vendors_sync_patch200_response_errors_inner_instance.to_dict()
# create an instance of RestV10VendorsSyncPatch200ResponseErrorsInner from a dict
rest_v10_vendors_sync_patch200_response_errors_inner_from_dict = RestV10VendorsSyncPatch200ResponseErrorsInner.from_dict(rest_v10_vendors_sync_patch200_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


