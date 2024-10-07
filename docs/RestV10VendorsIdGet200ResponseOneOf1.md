# RestV10VendorsIdGet200ResponseOneOf1

Vendor Directory View

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**abbreviated_name** | **str** | Abbreviated name | [optional] 
**address** | **str** | Address | [optional] 
**attachments** | [**List[NormalViewAttachmentsInner]**](NormalViewAttachmentsInner.md) | Attachments | [optional] 
**authorized_bidder** | **bool** | Authorized bidder status | [optional] 
**business** | [**RestV10VendorsIdGet200ResponseOneOf1AllOfBusiness**](RestV10VendorsIdGet200ResponseOneOf1AllOfBusiness.md) |  | [optional] 
**business_id** | **str** | Business id | [optional] 
**business_phone** | **str** | Business phone | [optional] 
**business_register** | [**NormalViewBusinessRegister**](NormalViewBusinessRegister.md) |  | [optional] 
**city** | **str** | City | [optional] 
**company_vendor** | **bool** |  | [optional] 
**contract_signer** | [**RestV10VendorsIdGet200ResponseOneOf1AllOfContractSigner**](RestV10VendorsIdGet200ResponseOneOf1AllOfContractSigner.md) |  | [optional] 
**country_name** | **str** |  | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**email_address** | **str** | Email address | [optional] 
**fax_number** | **str** | Fax number | [optional] 
**is_connected** | **bool** | Connected status | [optional] 
**labor_union** | **str** | Labor union | [optional] 
**legal_name** | **str** |  | [optional] 
**license_number** | **str** | License number | [optional] 
**logo** | **str** | Logo url | [optional] 
**mobile_phone** | **str** | Mobile phone | [optional] 
**non_union_prevailing_wage** | **bool** | Non union prevailing wage status | [optional] 
**notes** | **str** | Notes | [optional] 
**prequalified** | **bool** | Prequalified status | [optional] 
**primary_contact** | [**NormalViewPrimaryContact**](NormalViewPrimaryContact.md) |  | [optional] 
**state_code** | **str** | State code (ISO-3166 Alpha-2 format) | [optional] 
**state_name** | **str** |  | [optional] 
**trade_name** | **str** | Vendor&#39;s Trade Name, also known as Doing Business As (DBA). | [optional] 
**union_member** | **bool** | Union member status | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**website** | **str** | Website url | [optional] 
**zip** | **str** | Zip code | [optional] 
**invoice_contacts** | [**List[RestV10VendorsIdGet200ResponseOneOf1AllOfInvoiceContactsInner]**](RestV10VendorsIdGet200ResponseOneOf1AllOfInvoiceContactsInner.md) | Invoice Contacts | [optional] 
**trades** | [**List[Trade]**](Trade.md) | Trades | [optional] 
**standard_cost_codes** | [**List[RestV10VendorsIdGet200ResponseOneOf1AllOfStandardCostCodesInner]**](RestV10VendorsIdGet200ResponseOneOf1AllOfStandardCostCodesInner.md) |  | [optional] 
**bidding** | [**RestV10VendorsIdGet200ResponseOneOf1AllOfBidding**](RestV10VendorsIdGet200ResponseOneOf1AllOfBidding.md) |  | [optional] 
**bidding_distribution** | [**List[RestV10VendorsIdGet200ResponseOneOf1AllOfBiddingDistributionInner]**](RestV10VendorsIdGet200ResponseOneOf1AllOfBiddingDistributionInner.md) | Bidding Distribution List | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_vendors_id_get200_response_one_of1 import RestV10VendorsIdGet200ResponseOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10VendorsIdGet200ResponseOneOf1 from a JSON string
rest_v10_vendors_id_get200_response_one_of1_instance = RestV10VendorsIdGet200ResponseOneOf1.from_json(json)
# print the JSON string representation of the object
print(RestV10VendorsIdGet200ResponseOneOf1.to_json())

# convert the object into a dict
rest_v10_vendors_id_get200_response_one_of1_dict = rest_v10_vendors_id_get200_response_one_of1_instance.to_dict()
# create an instance of RestV10VendorsIdGet200ResponseOneOf1 from a dict
rest_v10_vendors_id_get200_response_one_of1_from_dict = RestV10VendorsIdGet200ResponseOneOf1.from_dict(rest_v10_vendors_id_get200_response_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


