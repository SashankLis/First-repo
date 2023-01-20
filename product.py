
def product_load():

        #   PRODUCT TABLE

        # truncate tmp table PRODUCT

        # truncate_tmp_product= '''
        #                              TRUNCATE TABLE BHATBHATENI.SASHANK_TMP.TMP_PRODUCT
        #                              '''
        #
        # sf.execute_query(truncate_tmp_product)

        # load tmp table PRODUCT

        load_temp_product= '''
                                      INSERT INTO BHATBHATENI.SASHANK_TMP.TMP_PRODUCT(
                                      PDT_ID,SUB_CTGRY_KY,PDT_DESC
                                      )
                                      SELECT PDT.ID, SUBC.SUB_CTGRY_KY, PDT.PRODUCT_DESC
                                      FROM BHATBHATENI.SASHANK_STG.STG_PRODUCT PDT
                                      LEFT JOIN BHATBHATENI.SASHANK_TGT.TGT_SUBCATEGORY SUBC
                                      ON PDT.SUBCATEGORY_ID = SUBC.SUB_CTGRY_KY
    
                                      '''
        sf.execute_query(load_temp_product)


        # load target table PRODUCT


        load_tgt_product = '''
                                      INSERT INTO BHATBHATENI.SASHANK_TGT.TGT_PRODUCT(
                                      PDT_KY,PDT_ID,SUB_CTGRY_KY,
                                      PDT_DESC,ACTV_FLG,PRICE,OPEN_CLOSE_CD,ROW_INSRT_TMS,ROW_UPDT_TMS
                                      )
                                      SELECT PDT_KY,PDT_ID, SUB_CTGRY_KY, PDT_DESC,
                                      1,NULL, 1, LOCALTIMESTAMP,LOCALTIMESTAMP
                                      FROM BHATBHATENI.SASHANK_TMP.TMP_PRODUCT
                                      WHERE PDT_ID NOT IN (SELECT DISTINCT PDT_ID FROM BHATBHATENI.SASHANK_TGT.TGT_PRODUCT)
                                      '''
        sf.execute_query(load_tgt_product)

        # update target table PRODUCT

        # update_tgt_product = '''
        #                                   UPDATE BHATBHATENI.SASHANK_TGT.TGT_PRODUCT T1
        #                                   SET T1.SUB_CTGRY_KY = T2.SUB_CTGRY_KY,
        #                                   T1.PDT_DESC = T2.PDT_DESC,
        #                                   ROW_UPDT_TMS = LOCALTIMESTAMP
        #                                   FROM BHATBHATENI.SASHANK_TMP.TMP_PRODUCT T2
        #                                   WHERE T1.PDT_ID = T2.PDT_ID;
        #                                   '''
        # sf.execute_query(update_tgt_product)

