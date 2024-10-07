# Body125BimPlanOneOf1

BIM Plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_level_id** | **int** | ID of the BIM Level to be associated to the plan | 
**drawing_id** | **int** | ID of the Drawing to be associated to the plan | [optional] 
**upload_uuid** | **str** | UUID of uploaded 2D sheet image. One of drawing_id or upload_uid is required | [optional] 
**sheet_map_start** | [**RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart**](RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart.md) |  | [optional] 
**sheet_map_end** | [**RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart**](RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart.md) |  | [optional] 
**model_map_start** | [**RestV10BimPlansGet200ResponseInnerAllOfModelMapStart**](RestV10BimPlansGet200ResponseInnerAllOfModelMapStart.md) |  | [optional] 
**model_map_end** | [**RestV10BimPlansGet200ResponseInnerAllOfModelMapStart**](RestV10BimPlansGet200ResponseInnerAllOfModelMapStart.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body125_bim_plan_one_of1 import Body125BimPlanOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of Body125BimPlanOneOf1 from a JSON string
body125_bim_plan_one_of1_instance = Body125BimPlanOneOf1.from_json(json)
# print the JSON string representation of the object
print(Body125BimPlanOneOf1.to_json())

# convert the object into a dict
body125_bim_plan_one_of1_dict = body125_bim_plan_one_of1_instance.to_dict()
# create an instance of Body125BimPlanOneOf1 from a dict
body125_bim_plan_one_of1_from_dict = Body125BimPlanOneOf1.from_dict(body125_bim_plan_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


