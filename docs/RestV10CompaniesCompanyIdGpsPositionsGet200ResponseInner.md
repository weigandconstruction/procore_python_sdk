# RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**company_id** | **int** |  | [optional] 
**latitude** | **float** | The latitude in degrees. | [optional] 
**longitude** | **float** | The longitude in degrees. | [optional] 
**altitude** | **float** | The altitude, measured in meters. | [optional] 
**horizontal_accuracy** | **float** | The horizontal radius of uncertainty for the location, measured in meters. | [optional] 
**vertical_accuracy** | **float** | The vertical radius of uncertainty for the location, measured in meters. | [optional] 
**timestamp** | **datetime** | The time at which this location was determined. | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**created_at** | **datetime** | Date and time the gps position was created. | [optional] 
**updated_at** | **datetime** | Date and time the gps position was updated. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_gps_positions_get200_response_inner import RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_gps_positions_get200_response_inner_instance = RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_gps_positions_get200_response_inner_dict = rest_v10_companies_company_id_gps_positions_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner from a dict
rest_v10_companies_company_id_gps_positions_get200_response_inner_from_dict = RestV10CompaniesCompanyIdGpsPositionsGet200ResponseInner.from_dict(rest_v10_companies_company_id_gps_positions_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


