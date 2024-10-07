# RestV10CompaniesCompanyIdUomsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**is_standard** | **bool** | Unit of Measure is among the standard units provided by Procore by default | [optional] 
**name** | **str** | Name of Unit of Measure | [optional] 
**description** | **str** | Description of Unit of Measure | [optional] 
**uom_category** | [**RestV10CompaniesCompanyIdUomsGet200ResponseInnerUomCategory**](RestV10CompaniesCompanyIdUomsGet200ResponseInnerUomCategory.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_uoms_get200_response_inner import RestV10CompaniesCompanyIdUomsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdUomsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_uoms_get200_response_inner_instance = RestV10CompaniesCompanyIdUomsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdUomsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_uoms_get200_response_inner_dict = rest_v10_companies_company_id_uoms_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdUomsGet200ResponseInner from a dict
rest_v10_companies_company_id_uoms_get200_response_inner_from_dict = RestV10CompaniesCompanyIdUomsGet200ResponseInner.from_dict(rest_v10_companies_company_id_uoms_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


